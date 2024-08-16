from flask import request, jsonify
from app.models import db, Feedback, Sentiment, Requested_features

def create_feedback():
    data = request.get_json()
    feedback = data.get('feedback')
    
    new_feedback = Feedback(feedback=feedback)
    db.session.add(new_feedback)
    db.session.commit()
    
    return jsonify({"message": "Feedback criado com successo", "feedback": feedback}), 201

def get_feedbacks():
    feedbacks = Feedback.query.all()
    return jsonify([{"id": fb.id, "feedback": fb.feedback} for fb in feedbacks]), 200

def create_sentiment():
    data = request.get_json()
    sentiment = data.get('sentiment')
    feedback_id = data.get('feedback_id')
    requested_features_data = data.get('requested_features', [])

    new_sentiment = Sentiment(sentiment=sentiment, feedback_id=feedback_id)
    db.session.add(new_sentiment)
    db.session.flush()

    for feature in requested_features_data:
        code = feature.get('code')
        reason = feature.get('reason')
        new_feature = Requested_features(code=code, reason=reason, sentiment_id=new_sentiment.id)
        db.session.add(new_feature)

    db.session.commit()
    
    return jsonify({"message": "Sentimento criado com successo", "sentiment": sentiment}), 201

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
