from flask import request, jsonify
from app.models import db, Feedback, Sentiment, Requested_features
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

import json
from decouple import config

api_key = config("OPENAI_API_KEY")

def openai_analyzer():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return jsonify({'error': 'Tipo de conteúdo não suportado!'}), 415

    json_payload = request.json
    feedback = json_payload.get('feedback')

    if not feedback:
        return jsonify({"error": "Feedback não enviado!"}), 400

    feedback_id = post_feedback(feedback)
    prompt = create_prompt(feedback)
    response_json = get_llm_response(prompt)

    if 'error' in response_json:
        return jsonify(response_json), 500

    save_sentiment(response_json, feedback_id)

    return jsonify({
        "message": "Feedback e Sentimento adicionados ao banco com sucesso",
    }), 201

def get_feedbacks():
    feedbacks = Feedback.query.all()
    return jsonify([{"id": fb.id, "feedback": fb.feedback} for fb in feedbacks]), 200

def get_sentiments():
    sentiments = Sentiment.query.all()
    result = []
    for sentiment in sentiments:
        features = [
            {
                "code": rf.code,
                "reason": rf.reason
            }
            for rf in sentiment.requested_features
        ]
        result.append({
            "id": sentiment.id,
            "sentiment": sentiment.sentiment.upper(),
            "requested_features": features
        })
    
    return jsonify(result), 200

def post_feedback(feedback):
    new_feedback = Feedback(feedback=feedback)
    db.session.add(new_feedback)
    db.session.commit()
    return new_feedback.id

def create_prompt(feedback):
    prompt_template = """
    Você é treinado para analisar e detectar o sentimento de um texto fornecido para a startup AluraMind.

    Se o texto fornecido estiver desconexo ou aparentar não ter sentido, considere como um SPAM. Caso seja um SPAM, apenas ignore a requisição.

    Na análise determine se o sentimento é: “POSITIVO”, “NEGATIVO” ou “INCONCLUSIVO”.

    Retorne apenas um objeto JSON, formatado, contendo os atributos `sentiment`, `requested_features` que é uma lista de objetos com os atributos `code` e `reason`. Segue um exemplo de feedback:
    {{
        "sentiment": "POSITIVO",
        "requested_features": [
            {{
                "code": "EDITAR_PERFIL",
                "reason": "O usuário gostaria de realizar a edição do próprio perfil"
            }}
        ]
    }}
    
    Aqui está o texto para análise...
    {feedback}
    """
    return prompt_template.format(feedback=feedback)

def get_llm_response(prompt):
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    response = llm([HumanMessage(content=prompt)])

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {'error': 'Failed to decode response from LLM'}

def save_sentiment(response_json, feedback_id):
    sentiment = response_json.get('sentiment')
    requested_features_data = response_json.get('requested_features', [])

    new_sentiment = Sentiment(sentiment=sentiment, feedback_id=feedback_id)
    db.session.add(new_sentiment)
    db.session.flush()

    for feature in requested_features_data:
        code = feature.get('code')
        reason = feature.get('reason')
        new_feature = Requested_features(code=code, reason=reason, sentiment_id=new_sentiment.id)
        db.session.add(new_feature)

    db.session.commit()