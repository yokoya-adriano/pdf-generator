from fpdf import FPDF
import os
from .pdf_layout import apply_default_layout

def rebuild_pdf(title: str, content: dict, filename: str) -> str:
    pdf = FPDF()
    apply_default_layout(pdf, title, content)

    output_dir = "generated"
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)
    pdf.output(file_path)

    return file_path
