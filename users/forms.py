from django import forms
from django.core.exceptions import ValidationError
from users.models import User

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2: # проверка на пустоту
            if password1 != password2: # проверка на единство
                raise ValidationError(
                    'Пароли не совпадают'
                )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже зарегистрирован!')
        return email


class ConfirmEmailForm(forms.Form):
    code = forms.CharField(max_length=6)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



    