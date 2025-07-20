# legal_prompt_builder.py

import os
from datetime import datetime
from reportlab.pdfgen import canvas
from pdfminer.high_level import extract_text

from .ai_modules import create_prompt
from .ai_engine import generate_legal_document
from .models import PromptResponseLog  #  Add this import

def generate_document(file_path, action_type, use_openai=False):
    try:
        extracted_text = extract_text(file_path)
    except Exception as e:
        return f"Error extracting text: {e}"

    prompt = create_prompt(action_type, extracted_text)
    generated_text = generate_legal_document(prompt, use_openai=use_openai)

    # Save prompt and response to DB
    '''PromptResponseLog.objects.create(
        action_type=action_type,
        prompt_text=prompt,
        response_text=generated_text,
        file_name=os.path.basename(file_path)
    )'''

    os.makedirs("media/generated", exist_ok=True)
    output_path = f"media/generated/{action_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(output_path)
    y = 800

    for para in generated_text.split("\n"):
        lines = [para[i:i+90] for i in range(0, len(para), 90)]
        for line in lines:
            if y < 50:
                c.showPage()
                y = 800
            c.drawString(50, y, line)
            y -= 20

    c.save()
    return output_path
