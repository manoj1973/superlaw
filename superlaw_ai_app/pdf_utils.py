# superlaw_ai_app/pdf_utils.py
from fpdf import FPDF
import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlaw_django_project.settings")
def save_text_as_pdf(text, filename):
    output_dir = "C:/pdfoutputs"
    os.makedirs(output_dir, exist_ok=True)  # Automatically creates folder if not there
    print("after making diectory ")
    full_path = os.path.join(output_dir, filename)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(full_path)
    print(f"✅ PDF saved at: {full_path}")
    return full_path
