from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import io
import os

# Register Unicode font for Hindi support
font_path = os.path.join(os.path.dirname(__file__), "NotoSans-Regular.ttf")

if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont("NotoSans", font_path))
    BODY_FONT = "NotoSans"
else:
    BODY_FONT = "Helvetica"

# Always use Helvetica for title to avoid overlap
TITLE_FONT = "Helvetica-Bold"
BOLD_FONT = "Helvetica-Bold"


def generate_pdf_report(filename, transcript, language, meeting_summary):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Normal"],
        fontSize=20,
        textColor=colors.HexColor("#0c0c0f"),
        fontName=TITLE_FONT,
        spaceAfter=6,
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.HexColor("#888888"),
        fontName=BODY_FONT,
        spaceAfter=2,
    )

    section_style = ParagraphStyle(
        "Section",
        parent=styles["Normal"],
        fontSize=12,
        textColor=colors.HexColor("#1a1a1a"),
        fontName=BOLD_FONT,
        spaceBefore=16,
        spaceAfter=8,
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=9.5,
        textColor=colors.HexColor("#333333"),
        fontName=BODY_FONT,
        leading=15,
        spaceAfter=4,
    )

    speaker_name_style = ParagraphStyle(
        "SpeakerName",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.HexColor("#1a6b3c"),
        fontName=BOLD_FONT,
        spaceBefore=10,
        spaceAfter=2,
    )

    speaker_text_style = ParagraphStyle(
        "SpeakerText",
        parent=styles["Normal"],
        fontSize=9.5,
        textColor=colors.HexColor("#333333"),
        fontName=BODY_FONT,
        leading=15,
        leftIndent=12,
        spaceAfter=4,
    )

    footer_style = ParagraphStyle(
        "Footer",
        parent=styles["Normal"],
        fontSize=9,
        textColor=colors.HexColor("#aaaaaa"),
        fontName=BODY_FONT,
        alignment=1,  # center
        spaceBefore=20,
    )

    elements = []

    # ===== PAGE 1: HEADER + AI SUMMARY =====
    elements.append(Paragraph("MeetingMind", title_style))
    elements.append(Paragraph("AI Meeting Intelligence Report", subtitle_style))
    elements.append(Spacer(1, 8))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e0e0e0")))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"File: {filename}", subtitle_style))
    elements.append(Paragraph(f"Language: {language.upper()}", subtitle_style))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", subtitle_style))
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#eeeeee")))

    elements.append(Paragraph("AI Meeting Summary", section_style))

    for line in meeting_summary.split("\n"):
        line = line.strip()
        if not line:
            elements.append(Spacer(1, 4))
            continue
        line = line.replace("**", "").replace("##", "").replace("#", "")
        if line.startswith("- ") or line.startswith("* "):
            line = "• " + line[2:]
        elements.append(Paragraph(line, body_style))

    # Footer page 1
    elements.append(Spacer(1, 20))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#eeeeee")))
    elements.append(Paragraph("Prepared via MeetingMind by Akhil Himnad", footer_style))

    # ===== PAGE 2: SPEAKER DIALOGUE TRANSCRIPT =====
    elements.append(PageBreak())

    elements.append(Paragraph("MeetingMind", title_style))
    elements.append(Paragraph("Speaker Dialogue Transcript", subtitle_style))
    elements.append(Spacer(1, 8))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e0e0e0")))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"File: {filename}", subtitle_style))
    elements.append(Paragraph(f"Language: {language.upper()}", subtitle_style))
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#eeeeee")))
    elements.append(Spacer(1, 8))

    # Parse speaker transcript
    if "SPEAKER_" in transcript:
        lines = transcript.strip().split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("SPEAKER_"):
                parts = line.split(":", 1)
                if len(parts) == 2:
                    speaker = parts[0].strip()
                    try:
                        num = int(speaker.split("_")[1]) + 1
                        speaker_label = f"Speaker {num}"
                    except Exception:
                        speaker_label = speaker
                    dialogue = parts[1].strip()
                    elements.append(Paragraph(f"Speaker {num}", speaker_name_style))
                    elements.append(Paragraph(dialogue, speaker_text_style))
                    elements.append(HRFlowable(
                        width="100%", thickness=0.3,
                        color=colors.HexColor("#f0f0f0")
                    ))
            else:
                elements.append(Paragraph(line, body_style))
    else:
        elements.append(Paragraph("Full Transcript", section_style))
        elements.append(Paragraph(transcript, body_style))

    # Footer page 2
    elements.append(Spacer(1, 20))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#eeeeee")))
    elements.append(Paragraph("Prepared via MeetingMind by Akhil Himnad", footer_style))

    doc.build(elements)
    buffer.seek(0)
    return buffer