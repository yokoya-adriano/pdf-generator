# 🧾 PDF Generator API com FastAPI

Esta aplicação é uma API REST feita com **FastAPI** que permite:

- Gerar um arquivo **PDF** a partir de um JSON enviado via `POST`
- Salvar o conteúdo do JSON em um arquivo `.json`
- Fazer o **download do PDF** posteriormente via rota `GET`

---

## 📦 Requisitos

- Python 3.10+
- Git
- Linux ou Windows recomenda-se usar **WSL**

---

## ▶️ Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/yokoya-adriano/pdf-generator.git
cd pdf-generator
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Rode a aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

---

## 🚀 Endpoints disponíveis

### `POST /generate-pdf`

Gera um PDF e salva os dados como `.json`

- **Body JSON**:

```json
{
  "title": "Relatório Semanal",
  "content": "Conteúdo do relatório.\nCom múltiplas linhas."
}
```

- **Retorno**:

```json
{
  "filename": "Relatorio_Semanal_20250710_153000.pdf"
}
```

---

### `GET /download-pdf/{filename}`

Permite baixar o PDF gerado (pelo nome retornado anteriormente)

Exemplo:

```
GET /download-pdf/Relatorio_Semanal_20250710_153000.pdf
```

---

## 🗂 Estrutura de arquivos gerados

- `generated/` → onde os PDFs são salvos
- `generated_json/` → onde os arquivos `.json` com o conteúdo original são salvos

---

## 📘 Tecnologias usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [FPDF](https://py-pdf.github.io/fpdf2/)

---

## 💡 Melhorias futuras

- Adicionar autenticação (JWT)
- Listar arquivos já gerados
- Exportar conteúdo em HTML
- Enviar PDF por e-mail
