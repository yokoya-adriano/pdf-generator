from fpdf import FPDF
import os
import re
from datetime import datetime
import json

def sanitize_filename(filename: str) -> str:
    """
    Remove caracteres inválidos do nome do arquivo e substitui espaços por underlines.
    """
    return re.sub(r'[^\w\-_.]', '_', filename)

def generate_pdf(title: str, content: str) -> str:
    """
    Gera um arquivo PDF com título e conteúdo fornecidos.
    O arquivo é salvo em disco e o caminho é retornado.
    """
    # Cria o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título centralizado
    pdf.cell(200, 10, txt=title, ln=True, align='C')

    # Conteúdo
    pdf.multi_cell(0, 10, txt=content)

    #### PDF ####
    # Cria diretório "generated" se ainda não existir
    output_dir = "generated"
    os.makedirs(output_dir, exist_ok=True)

    # Cria nome seguro + timestamp
    safe_title = sanitize_filename(title)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_title}_{timestamp}.pdf"

    # Caminho completo
    file_path = os.path.join(output_dir, filename)

    # Salva o arquivo PDF
    pdf.output(file_path)

    #### JSON ####
    # Diretório para JSON
    json_output_dir = "generated_json"
    os.makedirs(json_output_dir, exist_ok=True)

    # Caminho do arquivo JSON com o mesmo nome do PDF
    json_file_path = os.path.join(json_output_dir, filename.replace(".pdf", ".json"))

    # Dados da requisição a serem salvos
    data_dict = {
        "title": title,
        "content": content
    }

    # Salva o JSON
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, ensure_ascii=False, indent=2)

    return file_path
