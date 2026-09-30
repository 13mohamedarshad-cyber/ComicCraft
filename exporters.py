from pathlib import Path
from datetime import datetime
from fpdf import FPDF

EXPORT_DIR = Path("app/static/exports")
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

def save_pdf(layout):
    filename = f"comic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    output = EXPORT_DIR / filename

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for panel in layout:
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.multi_cell(0, 10, str(panel["title"]))

        if panel.get("image_path"):
            local_path = panel["image_path"].replace("/static/", "app/static/")
            if Path(local_path).exists():
                pdf.image(local_path, x=15, y=35, w=180)
                pdf.ln(125)

        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 7, f"Scene: {panel['scene_description']}")
        pdf.ln(3)
        pdf.multi_cell(0, 7, panel["story"])

    pdf.output(str(output))
    return f"/static/exports/{filename}"
