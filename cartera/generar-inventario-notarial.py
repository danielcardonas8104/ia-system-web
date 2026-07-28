from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether)

OUT = "/home/user/ia-system-web/cartera/Inventario-seguros-vida-Daniel-Cardona-Sanchez-2026-07-28.pdf"

INK = colors.HexColor("#111827")
SLATE = colors.HexColor("#334155")
MUTED = colors.HexColor("#6B7280")
RULE = colors.HexColor("#D1D5DB")
BAND = colors.HexColor("#F3F4F6")
ALERT = colors.HexColor("#92400E")
ALERTBG = colors.HexColor("#FEF7EC")

ss = getSampleStyleSheet()

def S(name, **kw):
    base = dict(name=name, fontName="Helvetica", fontSize=9.5, leading=13.5,
                textColor=INK, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(**base)

TitleS   = S("t", fontName="Helvetica-Bold", fontSize=17, leading=21, spaceAfter=3)
SubS     = S("s", fontSize=10.5, leading=14, textColor=MUTED, spaceAfter=2)
H1       = S("h1", fontName="Helvetica-Bold", fontSize=11, leading=14,
             spaceBefore=13, spaceAfter=6)
Body     = S("b", alignment=TA_JUSTIFY, spaceAfter=6)
Small    = S("sm", fontSize=8.5, leading=11.5, textColor=MUTED, alignment=TA_JUSTIFY)
Cell     = S("c", fontSize=8.8, leading=11.5)
CellB    = S("cb", fontSize=8.8, leading=11.5, fontName="Helvetica-Bold")
CellR    = S("cr", fontSize=8.8, leading=11.5, alignment=TA_RIGHT)
CellRB   = S("crb", fontSize=8.8, leading=11.5, alignment=TA_RIGHT,
             fontName="Helvetica-Bold")
Head     = S("hd", fontSize=8.3, leading=10.5, fontName="Helvetica-Bold",
             textColor=colors.white)
HeadR    = S("hdr", fontSize=8.3, leading=10.5, fontName="Helvetica-Bold",
             textColor=colors.white, alignment=TA_RIGHT)
AlertS   = S("al", fontSize=9, leading=12.5, textColor=ALERT, alignment=TA_JUSTIFY)


def header_footer(canv, doc):
    canv.saveState()
    w, h = letter
    canv.setStrokeColor(RULE)
    canv.setLineWidth(0.5)
    canv.line(20*mm, h - 15*mm, w - 20*mm, h - 15*mm)
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(MUTED)
    canv.drawString(20*mm, h - 13*mm, "Inventario de seguros de vida vigentes")
    canv.drawRightString(w - 20*mm, h - 13*mm, "Daniel Cardona Sánchez")
    canv.line(20*mm, 16*mm, w - 20*mm, 16*mm)
    canv.setFont("Helvetica", 7)
    canv.drawString(20*mm, 12*mm,
                    "Documento informativo. No constituye constancia oficial "
                    "ni certificación emitida por la aseguradora.")
    canv.drawRightString(w - 20*mm, 12*mm, "Página %d" % canv.getPageNumber())
    canv.restoreState()


def table(rows, widths, align_right=(), total_row=False):
    data = []
    for i, r in enumerate(rows):
        out = []
        for j, c in enumerate(r):
            if i == 0:
                st = HeadR if j in align_right else Head
            elif total_row and i == len(rows) - 1:
                st = CellRB if j in align_right else CellB
            else:
                st = CellR if j in align_right else Cell
            out.append(Paragraph(str(c), st))
        data.append(out)
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), SLATE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 1), (-1, -2 if total_row else -1), 0.4, RULE),
    ]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            cmds.append(("BACKGROUND", (0, i), (-1, i), BAND))
    if total_row:
        cmds += [("LINEABOVE", (0, -1), (-1, -1), 0.9, SLATE),
                 ("BACKGROUND", (0, -1), (-1, -1), colors.white)]
    t.setStyle(TableStyle(cmds))
    return t


def callout(title, body_text):
    inner = [[Paragraph("<b>%s</b>" % title, AlertS)],
             [Paragraph(body_text, AlertS)]]
    t = Table(inner, colWidths=[171*mm], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ALERTBG),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#E0B980")),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 9),
        ("TOPPADDING", (0, 1), (-1, -1), 2),
    ]))
    return t


st = []
A = st.append

A(Paragraph("Inventario de seguros de vida vigentes", TitleS))
A(Paragraph("Documento preparado para trámite notarial", SubS))
A(Spacer(1, 9))

A(Paragraph("1. Datos del titular", H1))
A(table([
    ["Concepto", "Dato"],
    ["Nombre", "Daniel Cardona Sánchez"],
    ["Fecha de nacimiento", "16 de abril de 1981"],
    ["Aseguradora", "Prudential Seguros México, S.A. de C.V."],
    ["Número de pólizas vigentes", "4"],
    ["Fecha de elaboración", "28 de julio de 2026"],
], [55*mm, 116*mm]))

A(Paragraph("2. Naturaleza y alcance de este documento", H1))
A(Paragraph(
    "Este documento es un resumen informativo elaborado por el titular a partir de la "
    "consulta directa al portal de la aseguradora en la fecha indicada. "
    "<b>No constituye carátula, constancia de vigencia, ni certificación emitida por "
    "Prudential Seguros México</b>, y no sustituye a los documentos originales de cada póliza. "
    "Su propósito es facilitar la identificación de las pólizas para efectos del trámite "
    "notarial correspondiente.", Body))
A(Paragraph(
    "Para cualquier efecto legal o probatorio deberán solicitarse a la aseguradora las "
    "carátulas originales y las constancias de vigencia de cada póliza, conforme se detalla "
    "en la sección 7.", Body))

A(Paragraph("3. Consideración relevante para el notario", H1))
A(callout(
    "Los seguros de vida con beneficiario designado suelen quedar fuera de la masa hereditaria",
    "Conforme al régimen aplicable a los contratos de seguro en México, la suma asegurada por "
    "fallecimiento se paga directamente a los beneficiarios designados en la póliza, sin pasar "
    "por el procedimiento sucesorio. En cambio, sí pueden tener implicaciones patrimoniales: "
    "(i) las pólizas sin beneficiario designado o cuyo beneficiario sea la sucesión; "
    "(ii) el valor de rescate acumulado de las pólizas en las que el titular es contratante. "
    "Se solicita al notario confirmar el tratamiento aplicable a cada caso una vez verificada "
    "la designación de beneficiarios, la cual está pendiente de recabar."))
A(Spacer(1, 8))

sec4 = []
B = sec4.append
B(Paragraph("4. Pólizas vigentes: suma asegurada por fallecimiento", H1))
B(Paragraph(
    "Titular como asegurado y contratante en las cuatro pólizas. Todas con estatus "
    "<b>EN VIGOR</b> y pago de primas en curso a la fecha de elaboración. Las cifras de esta "
    "tabla corresponden a la cobertura básica, es decir, la que se paga por fallecimiento "
    "derivado de cualquier causa.", Body))
B(table([
    ["Póliza", "Producto", "Emisión", "Moneda", "Suma asegurada", "Equivalente MXN"],
    ["89793", "Bienestar Prudential 20 Años sin Invalidez", "02/07/2024", "UDIS",
     "150,000.00", "1,324,625"],
    ["102239", "Personaliza Pru 20 Años", "30/10/2025", "UDIS",
     "60,000.00", "529,850"],
    ["102261", "Garantía Prudential 20 Años sin Invalidez", "30/10/2025", "UDIS",
     "225,000.00", "1,986,937"],
    ["102264", "Bienestar Prudential 5 Años sin Invalidez", "30/10/2025", "USD",
     "113,300.00", "1,984,223"],
    ["Total", "", "", "", "", "5,825,634"],
], [17*mm, 62*mm, 20*mm, 17*mm, 27*mm, 28*mm],
    align_right=(4, 5), total_row=True))
B(Spacer(1, 5))
B(Paragraph(
    "Bases de valuación: UDI a 8.830830 pesos y tipo de cambio FIX de 17.5130 pesos por dólar "
    "publicado en el Diario Oficial de la Federación. Ambos valores son variables y deben "
    "reconfirmarse a la fecha en que se utilicen. La conversión se presenta únicamente como "
    "referencia; las obligaciones de la aseguradora están denominadas en UDIS y en dólares "
    "según corresponda.", Small))
A(KeepTogether(sec4))

A(Paragraph("5. Coberturas adicionales", H1))
A(Paragraph(
    "Las siguientes coberturas son beneficios independientes y no se acumulan a la suma "
    "asegurada básica por fallecimiento por cualquier causa. La cobertura por muerte accidental "
    "se suma a la básica únicamente cuando el fallecimiento es de origen accidental.", Body))
A(table([
    ["Póliza", "Invalidez total y permanente", "Muerte accidental", "Coberturas de salud"],
    ["89793", "150,000.00 UDIS", "150,000.00 UDIS", "Cirugías Bronce: 40,000.00 UDIS"],
    ["102239", "200,000.00 UDIS", "200,000.00 UDIS", "Ninguna"],
    ["102261", "225,000.00 UDIS", "225,000.00 UDIS", "Ninguna"],
    ["102264", "113,300.00 USD", "113,300.00 USD", "Ninguna"],
], [17*mm, 46*mm, 38*mm, 70*mm]))
A(Spacer(1, 6))
A(Paragraph(
    "Suma asegurada total en el supuesto de fallecimiento accidental, equivalente a la cobertura "
    "básica más la cobertura por muerte accidental: <b>12,887,584 pesos</b> en las mismas bases "
    "de valuación indicadas en la sección 4.", Body))

A(Paragraph("6. Anexo informativo: pólizas del grupo familiar", H1))
A(Paragraph(
    "Se relacionan a continuación las pólizas contratadas por el cónyuge del titular, en las que "
    "el titular no es contratante ni asegurado. Se incluyen únicamente para dar contexto "
    "patrimonial familiar y no forman parte del inventario del titular.", Body))
A(table([
    ["Póliza", "Contratante", "Asegurado", "Producto", "Suma asegurada", "Equiv. MXN"],
    ["92834", "Martha Leticia Gosserez Rojas", "Martha Leticia Gosserez Rojas",
     "Bienestar Prudential 10 Años", "250,000.00 UDIS", "2,207,708"],
    ["100631", "Martha Leticia Gosserez Rojas", "Aldo Cardona Gosserez",
     "Personaliza Pru 20 Años", "60,000.00 UDIS", "529,850"],
], [16*mm, 37*mm, 31*mm, 37*mm, 26*mm, 24*mm], align_right=(4, 5)))

A(Paragraph("7. Información pendiente de recabar", H1))
A(Paragraph(
    "Los siguientes elementos no pudieron documentarse en la consulta y se recomienda "
    "solicitarlos a la aseguradora antes de formalizar el trámite.", Body))
A(table([
    ["#", "Elemento pendiente", "Relevancia para el trámite"],
    ["1", "Designación de beneficiarios de cada póliza",
     "Determina si la suma asegurada se paga fuera de la sucesión. Es el dato de mayor "
     "relevancia notarial y actualmente no está documentado."],
    ["2", "Valor de rescate acumulado de cada póliza",
     "Puede constituir un derecho patrimonial del contratante con efectos en la sucesión."],
    ["3", "Vigencia de la póliza 102264",
     "El producto se denomina 5 Años. Falta confirmar si se refiere al periodo de pago de "
     "primas o a la vigencia de la cobertura."],
    ["4", "Carátulas y constancias de vigencia",
     "Documentos oficiales con valor probatorio que sustituyen a este resumen."],
], [8*mm, 55*mm, 108*mm]))

A(Paragraph("8. Declaración del titular", H1))
A(Paragraph(
    "El suscrito manifiesta que la información contenida en el presente documento fue obtenida "
    "de la consulta directa a los registros de la aseguradora en la fecha señalada, y que se "
    "presenta de buena fe como apoyo al trámite notarial, sin que constituya manifestación bajo "
    "protesta de decir verdad ni sustituya la documentación oficial correspondiente.", Body))
A(Spacer(1, 26))

sig = Table([
    [Paragraph("", Cell)],
    [Paragraph("Daniel Cardona Sánchez", CellB)],
    [Paragraph("Titular", Small)],
], colWidths=[85*mm], hAlign="LEFT")
sig.setStyle(TableStyle([
    ("LINEBELOW", (0, 0), (0, 0), 0.6, INK),
    ("TOPPADDING", (0, 0), (-1, -1), 2),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
]))
A(sig)

doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=22*mm, bottomMargin=22*mm,
    title="Inventario de seguros de vida vigentes - Daniel Cardona Sánchez",
    author="Daniel Cardona Sánchez",
    subject="Inventario de seguros de vida para tramite notarial",
)
doc.build(st, onFirstPage=header_footer, onLaterPages=header_footer)
print("OK ->", OUT)
