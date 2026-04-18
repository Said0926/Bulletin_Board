from django import forms
from .models import Response, Bulletin

class ResponseForm(forms.ModelForm):
    class Meta: # это настройки формы
        model = Response # с какой моделю работает эта форма 
        fields = ['text'] # в этой форме будет только поле текст
        # добавляем виджет (как будет выглядить наша форма точнее наше поле текст)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Напишите ваш отклик...'
            })
        }
        labels = {
            'text': 'Ваш отклик'
        }

class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ['title', 'text', 'category']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название объявления'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            })
        }