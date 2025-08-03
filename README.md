# API de Relatórios - Flask + Swagger

Este projeto é uma API RESTful desenvolvida com **Flask**, voltada para consulta de relatórios técnicos em um banco de dados relacional.

Ideal para sistemas corporativos que precisam expor dados com documentação clara e arquitetura profissional.

---

## 🚀 Tecnologias Utilizadas

- **Flask**: microframework para construção da API
- **Flasgger**: geração automática de documentação Swagger
- **SQLAlchemy**: ORM para manipulação de dados
- **SQLite** (pode ser facilmente adaptado para PostgreSQL ou Oracle)
- **Blueprints**: organização modular das rotas
- **dotenv**: gerenciamento de variáveis de ambiente

---

## 📁 Estrutura do Projeto

```
api_relatorios/
│
├── app.py                  # Ponto de entrada da aplicação
├── config/                 # Configurações de ambiente
│   └── settings.py
├── models/                 # Modelos SQLAlchemy
│   └── relatorio.py
├── controllers/            # Lógica de negócio
│   └── relatorio_controller.py
├── routes/                 # Rotas e documentação Swagger
│   └── relatorio_routes.py
├── services/               # Serviços auxiliares
├── utils/                  # Utilitários (formatação, validações, etc.)
├── static/                 # Swagger UI estática (Flasgger)
├── requirements.txt        # Dependências Python
└── .env.example            # Exemplo de configuração
```

---

## 🔧 Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/usuario/api-relatorios.git
cd api-relatorios

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env
# edite o arquivo .env conforme necessário (ex: caminho do banco SQLite)

# Rode a aplicação
python app.py
```

---

## 📘 Documentação Swagger

Após subir o servidor localmente:

📄 Acesse a documentação interativa em:

```
http://localhost:5000/apidocs/
```

---

## ✅ Funcionalidades

- Consulta de registros com filtros
- Estrutura pronta para expandir CRUD
- Documentação automática de todos os endpoints
- Padrão de respostas JSON estruturado
- Logs de requisições
- Suporte a múltiplos ambientes (dev, test, prod)

---

## 📌 Exemplo de Endpoint

`GET /api/relatorios?equipamento=TT01`

```json
[
  {
    "id": 1,
    "equipamento": "TT01",
    "data": "2025-07-25",
    "usuario": "jose",
    "status": "Finalizado"
  }
]
```

---

## 🧪 Testes

Você pode usar ferramentas como **Postman** ou **Swagger UI** incluído no projeto para testar todos os endpoints com segurança.

---

## 📄 Licença

Este projeto é open-source e pode ser utilizado como base para APIs corporativas, POCs ou integrações reais.

---

Desenvolvido por **Edvilson A. Kwiatkowski**  
[LinkedIn](https://linkedin.com) | [Portfólio](https://portfolio-edvilson.vercel.app)
