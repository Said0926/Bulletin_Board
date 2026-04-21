from django import forms
from .models import Newsletter
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'text': CKEditorUploadingWidget()
        }