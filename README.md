# Análise de Sentimentos Alumind

Este projeto é uma aplicação desenvolvida com Flask para realizar a análise de sentimentos de feedbacks de usuários. Ele utiliza a API da OpenAI para processar os textos fornecidos, determinando se o sentimento é `POSITIVO`, `NEGATIVO`, `INCONCLUSIVO` e `SPAM`, e identifica características específicas solicitadas pelos usuários.

![GIF que mostra o teste da rota de analise nos 4 tipos de retornos que ela pode apresentar](https://i.imgur.com/8aTVhJp.gif)

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

## Estrutura do Banco de Dados

Estrutura das tabelas que compõem o banco de dados. Ao longo do desenvolvimento do código, sofreram alguns pequenos ajustes nos relacionamentos entre si, mas nada que se difere da estrutura mostrada na imagem.

![Captura de tela de tabelas na plataforma do BRModelo Online](https://i.imgur.com/jg7npqL.png)

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
cd desafio_tecnico_alura
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

### 4. Apontar para aplicação o arquivo principal

Para ser possível rodar os próximos comandos é importante estabelecer para o ambiente da aplicação qual o arquivo principal da mesma, você pode fazer isso usando o seguinte comando:

**Windows**
```bash
$env:FLASK_APP="run.py"
```

ou

**Linux**
```bash
export FLASK_APP="run.py"
```

### 5. Criar as Tabelas no Banco de Dados

Para realizar a migrações das tabelas criadas no model do projeto, é necessário rodar o seguinte comando:

```bash
flask db upgrade
```

### 6. Executar a Aplicação

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

## Implementações Futuras

* Criar uma página frontend que lista os feedbacks com algum gráfico indicando a porcentagem de cada tipo: negativo, positivo, inconclusivo 

* Implementar a documentação completa para cobrir todos os aspectos da aplicação incluindo API modelos de dados, sem contar os exemplos de uso.

* Aplicar um sistema de segurança para proteger dados dos usuários com autenticação via JWT proteção contra ataques como SQL Injection e XSS e criptografia de dados sensíveis.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
