from django import forms
from django.forms import ClearableFileInput
from OCR712.models import Ocr712

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Ocr712
        fields = ['document', ]
        widgets = {
            'document': ClearableFileInput(attrs={'multiple': True}),
        }