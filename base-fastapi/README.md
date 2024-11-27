## Instruções para iniciar o projeto após o clone:

### Criar venv:

```bash
python -m venv .venv
```

### Entrar no venv:
- **Windows:**
```bash
.\.venv\Scripts\activate
```
- **Linux:**
```bash
source .venv/bin/activate
```

### Instalar as bibliotecas:
```bash
pip install -r requirements.txt
```

### Rodar:
```bash
uvicorn main:app --reload
```

### Criar um arquivo `.env` na raíz do projeto, com o conteúdo a seguir:
```ini
# Substitua pela url do seu banco:
DATABASE_URL = "postgresql://user:senha@localhost:5432/dbname"
```
