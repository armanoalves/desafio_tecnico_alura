# Projeto de Análise de Sentimentos

Este projeto é uma aplicação desenvolvida com Flask para realizar a análise de sentimentos de feedbacks de usuários. Ele utiliza a API da OpenAI para processar os textos fornecidos, determinando se o sentimento é `POSITIVO`, `NEGATIVO` ou `INCONCLUSIVO`, e identifica características específicas solicitadas pelos usuários.

## Funcionalidades

- Recebe feedbacks de usuários via API.
- Análise de sentimentos usando a API da OpenAI.
- Armazena feedbacks, sentimentos e características solicitadas em um banco de dados.
- Retorna os resultados da análise em formato JSON.

## Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Flask**: Framework web.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **OpenAI API**: Para análise de sentimentos.
- **PostgreSQL**: Banco de dados relacional.
- **Postman**: Para testar as rotas da API.

## Requisitos

- Python 3.12.3
- PostgreSQL

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
projeto-analise-sentimentos/
│
├── app/
│   ├── __init__.py           # Configurações iniciais do Flask, SQLAlchemy e outras extensões
│   ├── controllers.py        # Controladores que gerenciam as rotas e a lógica de negócio
│   ├── models.py             # Definições dos modelos de banco de dados
│   └── routes.py             # Definição das rotas da aplicação
│
├── migrations/               # Migrações do banco de dados geradas pelo Flask-Migrate
│
├── venv/                     # Ambiente virtual para as dependências do projeto
│
├── .env                      # Arquivo de configuração das variáveis de ambiente
├── .gitignore                # Arquivo que especifica quais arquivos/directórios ignorar pelo Git
├── config.py                 # Configurações da aplicação
├── LICENSE                   # Licença do projeto
├── README.md                 # Documentação do projeto (este arquivo)
├── requirements.txt          # Lista de dependências do projeto
└── run.py                    # Script para rodar o servidor Flask
```

## Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/armanoalves/desafio_tecnico_alura.git
cd projeto-analise-sentimentos
```

### 2. Instalar Dependências

Utilize o comando abaixo para instalar todas as dependências necessárias para executar o projeto:

```bash
pip install -r requirements.txt
```

### 3. Configurar as Variáveis de Ambiente

Preencha o arquivo `.env` com as informações necessárias para conectar ao banco de dados e utilizar a API da OpenAI. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```env
DB_USERNAME=seu_usuario_do_banco
DB_PASSWORD=sua_senha_do_banco
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=nome_do_seu_banco

OPENAI_API_KEY=sua_api_key
```

### 4. Executar a Aplicação

Após configurar as variáveis de ambiente, execute o comando abaixo para iniciar o servidor Flask:

```bash
python .\run.py runserver
```

O servidor será iniciado e a aplicação estará disponível em `http://localhost:5000`.

## Endpoints

### 1. Analisar Feedback

**POST** `/openai_analizer`

**CASO 1**

- **Descrição**: Envia um feedback para análise de sentimentos e adiciona o feedback e o sentimento gerado ao banco de dados.
- **Corpo da Requisição**:

  ```json
  {
    "feedback": "Exemplo de feedback para análise."
  }
  ```

- **Resposta**:

  ```json
  {
    "message": "Feedback e Sentimento adicionados ao banco com sucesso"
  }
  ```

**CASO 2**

- **Descrição**: Caso em que o Feedback analisado é reconhecido como um SPAM.
- **Corpo da Requisição**:

  ```json
  {
    "feedback": "Coisas aleatórias escritas aqui"
  }
  ```

- **Resposta**:

  ```json
  {
    "message": "SPAM reconhecido, feedback e sentimento não foram adicionados ao banco"
  }
  ```

### 2. Listar Feedbacks

**GET** `/feedbacks`

- **Descrição**: Retorna o feedback enviado na requisição POST para análise.

- **Resposta**:

  ```json
  [
    {
      "id": 1,
      "feedback": "Exemplo de feedback para análise."
    }
  ]
  ```

### 3. Listar Sentimentos

**GET** `/sentiments`

- **Descrição**: Retorna o sentimento gerado na análise do feedback enviado.

- **Resposta**:

  ```json
  [
    {
      "id": 1,
      "sentiment": "POSITIVO",
      "requested_features": [
        {
          "code": "EDITAR_PERFIL",
          "reason": "O usuário gostaria de realizar a edição do próprio perfil"
        }
      ]
    }
  ]
  ```

## Implementações futuras

Seria interessante implementar a **documentação completa** para cobrir **todos os aspectos da aplicação** incluindo API modelos de dados, sem contar os exemplos de uso. 

Também, aplicar um **sistema de segurança** para proteger dados dos usuários com **autenticação via JWT** proteção contra ataques como SQL Injection e XSS e **criptografia de dados sensíveis**.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
