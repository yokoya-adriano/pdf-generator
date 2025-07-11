from fpdf import FPDF

def apply_default_layout(pdf: FPDF, title: str, content: dict):
    """
    Aplica o layout padrão ao PDF.
    Recebe o FPDF, título e conteúdo como dict.
    """
    pdf.add_page()
    pdf.set_font("Arial", size=12, style='B')

    # Título centralizado
    pdf.cell(200, 10, txt=title, ln=True, align='C')

    # Espaço após título
    pdf.ln(10)

    # Cabeçalho da tabela
    pdf.set_font("Arial", style='B', size=12)
    pdf.set_fill_color(200, 200, 200)  # cinza claro
    pdf.cell(60, 10, "Campo", border=1, fill=True)
    pdf.cell(130, 10, "Valor", border=1, fill=True)
    pdf.ln()

    # Linhas da tabela
    pdf.set_font("Arial", size=12)
    for key, value in content.items():
        label = key.replace("_", " ").capitalize()
        pdf.cell(60, 10, label, border=1)
        pdf.cell(130, 10, value, border=1)
        pdf.ln()

