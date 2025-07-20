# superlaw/views.py

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .legal_prompt_builder import generate_document

def index(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        uploaded_file = request.FILES['pdf_file']
        action = request.POST.get('action_type')
        use_openai = bool(request.POST.get('use_openai'))

        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        full_path = fs.path(file_path)

        generated_path = generate_document(full_path, action, use_openai=use_openai)
        context['generated_file'] = generated_path

    return render(request, 'superlaw_ai_app/index.html', context)
