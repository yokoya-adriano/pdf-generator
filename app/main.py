from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.pdf_generator import generate_pdf
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Habilita o CORS para permitir chamadas do front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Você pode restringir aqui: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PDFContent(BaseModel):
    input_1: str
    input_2: str
    input_3: str

# Modelo da requisição (JSON)
class PDFRequest(BaseModel):
    title: str
    content: PDFContent

# Rota que gera e retorna o PDF
from fastapi.responses import JSONResponse

@app.post("/generate-pdf")
def create_pdf(data: PDFRequest):
    """
    Rota que recebe 'title' e 'content',
    gera um PDF local e retorna o nome do arquivo.
    """
    try:
        file_path = generate_pdf(data.title, data.content)
        filename = os.path.basename(file_path)

        # Retorna o nome do arquivo como JSON
        return JSONResponse(content={"filename": filename})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download-pdf/{filename}")
def download_pdf(filename: str):
    """
    Rota para download do PDF já gerado.
    """
    file_path = os.path.join("generated", filename)
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            media_type="application/pdf",
            filename=filename
        )
    raise HTTPException(status_code=404, detail="Arquivo não encontrado")


