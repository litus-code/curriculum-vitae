#!/usr/bin/env python3
"""Generate the published Carles Far OS CV (Retro Silver, Spanish, A4)."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

PAPER = HexColor("#F3F5FA")
INK = HexColor("#17233D")
BLUE = HexColor("#245BFF")
DARK_BLUE = HexColor("#163C9F")
LIGHT_BLUE = HexColor("#B7CCFD")
SILVER = HexColor("#DBE3F1")
BORDER = HexColor("#7387AC")
WHITE = colors.white
MARGIN = 34
W, H = A4

EXPERIENCE = [
    ("2026 - Actualidad", "EY / Radisson Hotels", "Lead Frontend",
     "Liderazgo del desarrollo frontend en Radisson Hotels con Vue, Nuxt, TypeScript y SSR; coordinación técnica y evolución del producto.", "EY"),
    ("2026", "Inditex / Bershka", "Senior Frontend Developer",
     "Desarrollo y mantenimiento de aplicaciones digitales para Bershka; nuevas funcionalidades y trabajo con Nuxt y Pinia.", "INDITEX"),
    ("2021 - 2025", "EY Barcelona", "Senior Frontend · Referente técnico",
     "Referente frontend del equipo AM; evolución y mantenimiento de un portal turístico con Vue 2, Nuxt y JavaScript.", "EY"),
    ("2020 - 2021", "T2CLIENT", "Frontend Developer · Referente de equipo",
     "Arquitectura de aplicaciones Vue 2/3 para logística; componentes Storybook y gestión de datos JSON.", "T2"),
    ("2020", "Coneptum AI", "Frontend Developer",
     "Desarrollo de una aplicación web para el sector del ocio con Vue 2 y Vuetify.", "AI"),
    ("2017 - 2019", "Casals Online", "Junior Frontend Developer",
     "Maquetación de landing pages y desarrollo JavaScript para marketing digital.", "CO"),
]

EDUCATION = [
    ("2019 - 2020", "Campus MVP",
     "Certificado de Programación avanzada con JavaScript y ECMAScript 6."),
    ("2016 - 2017", "ISDI Coders",
     "Bootcamp de desarrollo web full stack con JavaScript."),
    ("2013 - 2017", "STUCOM",
     "Formación de grado superior como Técnico Superior en Diseño y Desarrollo Web (DAW)."),
    ("2012 - 2013", "Universitat de Barcelona",
     "Prueba de acceso para mayores de 25 años a la universidad y/o formación de grado superior."),
]
TECH = ["Vue 2 / 3", "Nuxt 2 / 3 / 4", "TypeScript", "JavaScript", "Pinia / Vuex",
        "SSR", "Tailwind", "SCSS", "HTML / CSS", "Jest", "Storybook", "Git", "CI/CD"]
PROJECTS = [
    ("Cuebooker", "Plataforma de gestión de bookings para DJs, managers y agencias.", "Producto propio"),
    ("Friends Invisible", "Sorteos de amigo invisible, invitaciones y listas de deseos.", "En construcción"),
    ("Cuebooker DJ", "Aplicación de mezcla DJ, stems y compatibilidad con controladoras.", "En construcción"),
]


def font_setup() -> None:
    for name, location in (
        ("PixelRegular", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
        ("PixelBold", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"),
    ):
        if Path(location).exists():
            pdfmetrics.registerFont(TTFont(name, location))
        else:
            raise RuntimeError(f"Font missing: {location}")


def paragraph(c: Canvas, text: str, x: float, top: float,
              width: float, size: float = 8.4, leading: float = 12.4,
              color=INK, bold: bool = False) -> float:
    style = ParagraphStyle(
        "p", fontName="PixelBold" if bold else "PixelRegular",
        fontSize=size, leading=leading, textColor=color, spaceAfter=0,
        allowWidows=0, allowOrphans=0,
    )
    p = Paragraph(text, style)
    _, h = p.wrap(width, H)
    p.drawOn(c, x, top - h)
    return h


def card(c: Canvas, x: float, y: float, w: float, h: float, fill=WHITE) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(BORDER)
    c.setLineWidth(1.1)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)


def pill(c: Canvas, label: str, x: float, y: float, w: float,
         h: float = 20, fill=LIGHT_BLUE, color=INK, size=8.3) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(BORDER)
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
    c.setFillColor(color)
    c.setFont("PixelBold", size)
    c.drawCentredString(x + w / 2, y + (h-size)/2 + 1.4, label)


def section(c: Canvas, title: str, top: float) -> float:
    c.setFillColor(INK)
    c.setFont("PixelBold", 15)
    c.drawString(MARGIN, top, title)
    c.setFillColor(BLUE)
    c.rect(MARGIN, top - 8, 145, 3.5, fill=1, stroke=0)
    return top - 23


def page_base(c: Canvas, page: int) -> None:
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(SILVER)
    c.rect(0, H - 30, W, 30, fill=1, stroke=0)
    c.setStrokeColor(BORDER)
    c.line(0, H-30, W, H-30)
    c.setFillColor(INK)
    c.setFont("PixelBold", 9)
    c.drawString(MARGIN, H-20, "CARLES FAR OS")
    c.setFillColor(DARK_BLUE)
    c.drawRightString(W-MARGIN, H-20, "CURRICULUM VITAE / RETRO SILVER")
    c.setStrokeColor(BORDER)
    c.line(MARGIN, 32, W-MARGIN, 32)
    c.setFillColor(INK)
    c.setFont("PixelRegular", 8)
    c.drawString(MARGIN, 19, "carlesfar.com  ·  Barcelona")
    c.drawRightString(W-MARGIN, 19, f"CV 2.1 · {page}/2")


def photo(c: Canvas, portrait: Path, x: float, top: float, size: float) -> None:
    c.setFillColor(HexColor("#111831"))
    c.rect(x-3, top-size-3, size+6, size+6, fill=1, stroke=0)
    if portrait.exists():
        with Image.open(portrait) as image:
            image = image.convert("RGB").resize((320, 320), Image.Resampling.NEAREST)
            c.drawImage(ImageReader(image), x, top-size, size, size, mask="auto")
    else:
        c.setFillColor(BLUE)
        c.rect(x, top-size, size, size, fill=1, stroke=0)


def page_one(c: Canvas, portrait: Path) -> None:
    page_base(c, 1)
    top = H-49
    photo(c, portrait, MARGIN+5, top, 106)
    x = MARGIN+131
    c.setFillColor(INK)
    c.setFont("PixelBold", 29)
    c.drawString(x, top-33, "Carles Far")
    c.setFont("PixelBold", 10)
    c.drawString(x, top-55, "Frontend Lead &amp; Product Builder".replace("&amp;", "&"))
    paragraph(c, "Desarrollador frontend de Barcelona, con 10 años de experiencia "
              "creando aplicaciones y productos digitales.", x, top-65, W-MARGIN-x,
              size=8, leading=12)
    pill(c, "10 AÑOS DE EXPERIENCIA FRONTEND", x, top-108, 273, 20,
         fill=LIGHT_BLUE, size=8.5)

    c.setFillColor(DARK_BLUE)
    c.setFont("PixelRegular", 8)
    c.drawString(MARGIN+5, top-139,
        "contacto@carlesfar.com  ·  carlesfar.com  ·  linkedin.com/in/carles-far-pierres-390160139/")
    start = section(c, "EXPERIENCIA PROFESIONAL", top-170)
    row_h = 79
    gap = 7
    line_x = MARGIN+6
    c.setStrokeColor(BLUE)
    c.setLineWidth(2.6)
    c.line(line_x, start-13, line_x, start-(row_h+gap)*5-43)
    for idx, (dates, company, position, details, icon) in enumerate(EXPERIENCE):
        row_top = start - idx*(row_h+gap)
        row_y = row_top-row_h
        c.setFillColor(LIGHT_BLUE)
        c.setStrokeColor(DARK_BLUE)
        c.circle(line_x, row_y+row_h/2, 4.4, fill=1, stroke=1)
        pill(c, dates, MARGIN+18, row_y+row_h/2-11, 106, 22,
             fill=LIGHT_BLUE, size=7.0)
        box_x = MARGIN+135
        box_w = W-MARGIN-box_x
        card(c, box_x, row_y, box_w, row_h, fill=WHITE)
        c.setFillColor(LIGHT_BLUE)
        c.roundRect(box_x+9, row_y+22, 38, 37, 4, fill=1, stroke=0)
        c.setFillColor(DARK_BLUE)
        c.setFont("PixelBold", 10 if len(icon)<4 else 7)
        c.drawCentredString(box_x+28, row_y+36, icon)
        text_x = box_x+57
        c.setFillColor(INK)
        c.setFont("PixelBold", 10.1)
        c.drawString(text_x, row_top-16, company)
        c.setFillColor(DARK_BLUE)
        c.setFont("PixelBold", 8.0)
        c.drawString(text_x, row_top-31, position)
        paragraph(c, details, text_x, row_top-39, box_w-65,
                  size=6.9, leading=10)
    c.showPage()


def page_two(c: Canvas) -> None:
    page_base(c, 2)
    c.setFillColor(INK)
    c.setFont("PixelBold", 25)
    c.drawString(MARGIN, H-71, "Carles Far")
    c.setFillColor(DARK_BLUE)
    c.setFont("PixelBold", 10)
    c.drawString(MARGIN, H-91, "FORMACIÓN · TECNOLOGÍAS · PROYECTOS")
    top = section(c, "FORMACIÓN", H-125)
    col_gap=13
    cw=(W-2*MARGIN-col_gap)/2
    card_h=101
    for i,(dates,name,description) in enumerate(EDUCATION):
        col=i%2
        row=i//2
        x=MARGIN+col*(cw+col_gap)
        y=top-row*(card_h+12)-card_h
        card(c,x,y,cw,card_h)
        pill(c,dates,x+12,y+card_h-30,100,18,size=7.8)
        c.setFillColor(INK)
        c.setFont("PixelBold",10.6)
        c.drawString(x+12,y+card_h-49,name)
        paragraph(c,description,x+12,y+card_h-56,cw-24,
                  size=7.3,leading=11.2)
    tech_top=top-2*(card_h+12)-10
    section(c,"TECNOLOGÍAS",tech_top)
    x=MARGIN
    y=tech_top-53
    for item in TECH:
        width=max(49,pdfmetrics.stringWidth(item,"PixelBold",7.3)+19)
        if x+width>W-MARGIN:
            x=MARGIN
            y-=27
        pill(c,item,x,y,width,20,fill=WHITE,size=7.3)
        x+=width+8
    projects_top=y-37
    section(c,"PRODUCTOS PROPIOS",projects_top)
    for i,(name,description,status) in enumerate(PROJECTS):
        y=projects_top-97-i*73
        card(c,MARGIN,y,W-2*MARGIN,65,fill=WHITE)
        c.setFillColor(INK)
        c.setFont("PixelBold",10.5)
        c.drawString(MARGIN+11,y+45,name)
        label_w=123 if status=="En construcción" else 111
        pill(c,status,W-MARGIN-label_w-11,y+38,label_w,19,
             fill=LIGHT_BLUE if status!="En construcción" else SILVER,
             size=7.2)
        paragraph(c,description,MARGIN+12,y+33,W-2*MARGIN-24,
                  size=8,leading=12)
    c.showPage()


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="public/carles-far-cv.pdf")
    parser.add_argument("--portrait",default="public/portrait-carles-retro-silver.webp")
    args=parser.parse_args()
    dest=Path(args.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    font_setup()
    c=Canvas(str(dest),pagesize=A4,pageCompression=1)
    c.setTitle("Carles Far | Curriculum Vitae 2.1 | Retro Silver")
    c.setAuthor("Carles Far")
    page_one(c,Path(args.portrait))
    page_two(c)
    c.save()
    print(f"Generated: {dest} ({dest.stat().st_size} bytes)")


if __name__=="__main__":
    main()
