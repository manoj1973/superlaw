from django.contrib import admin

# Register your models here.
# superlaw/admin.py
from django.contrib import admin
from .models import PromptResponseLog

admin.site.register(PromptResponseLog)
