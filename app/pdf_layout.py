from fpdf import FPDF
from fpdf.fonts import FontFace

def apply_default_layout(pdf: FPDF, title: str, content: dict):
    """
    Aplica o layout padrão ao PDF.
    Recebe o FPDF, título e conteúdo como dict.
    """
    pdf.add_page(orientation="landscape", format="A4")
    pdf.set_font("Arial", size=12)

    blue = (0, 0, 255)
    headings_style = FontFace(emphasis="BOLD", color=blue)

    with pdf.table(col_widths=(1, 1, 1, 1), num_heading_rows=0, first_row_as_headings=False) as table:
        # Linha 1
        row = table.row()
        row.cell(text=title, colspan=2, rowspan=3, align='C', style=headings_style)
        row.cell("C1", colspan=2)

        # Linha 2
        row = table.row()
        row.cell("C2", colspan=2, rowspan=2)

        # Linha 3
        row = table.row()
        # colunas 3 e 4 já ocupadas pelo rowspan de "C2", então não adiciona nada aqui

        # (Opcional) Linha de dados normal — não faz parte do cabeçalho
        row = table.row()
        row.cell("Dado A", colspan=1)
        row.cell("Dado B", colspan=1)
        row.cell("Dado C", colspan=1)
        row.cell("Dado D", colspan=1)

        
        # # Título centralizado
        # pdf.cell(200, 10, txt=title, ln=True, align='C')

        # # Cabeçalho da tabela
        # pdf.set_font("Arial", style='B', size=12)
        # pdf.set_fill_color(200, 200, 200)  # cinza claro
        # pdf.cell(60, 10, "Campo", border=1, fill=True)
        # pdf.cell(130, 10, "Valor", border=1, fill=True)
        # pdf.ln()

        # # Linhas da tabela
        # pdf.set_font("Arial", size=12)
        # for key, value in content.items():
        #     label = key.replace("_", " ").capitalize()
        #     pdf.cell(60, 10, label, border=1)
        #     pdf.cell(130, 10, value, border=1)
        #     pdf.ln()

