# API Relatórios

API RESTful para cadastro e listagem de relatórios utilizando Flask + SQLite.

## Estrutura

```
api_relatorios/
│
├── app.py                  # Ponto de entrada da aplicação
├── models/                 # Modelos SQLAlchemy
│   └── relatorio.py
├── controllers/            # Lógica de negócio
│   └── relatorio_controller.py
├── routes/                 # Rotas e documentação Swagger
│   └── relatorio_routes.py
├── requirements.txt        # Dependências Python
└── .env.example            # Exemplo de configuração
```

## Instalação

```bash
git clone https://github.com/Edvilson/ed-api-rel-python-backend.git
cd api_relatorios
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
cp .env.example .env
```

## Execução

```bash
python app.py
```

Acesse a documentação Swagger em: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

Desenvolvido por **Edvilson A. Kwiatkowski**  
[LinkedIn](https://www.linkedin.com/in/edvilson-kwiatkowski/) | [Portfólio](https://portfolio-edvilson.vercel.app)

