from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from users.models import User
from .forms import RegisterForm, ConfirmEmailForm, LoginForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login


# заглушки — потом заполним логикой
class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegisterForm()
        return context

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user = User.objects.create_user(email=email, password=password1)
            user.generate_code()
            send_mail(
                'Подтверждение регистрации',
                f'Ваш код подтверждения: {user.confirmation_code}',
                'noreply@bulletinboard.com',
                [user.email]
            )
            request.session['confirm_email'] = email
            return redirect('confirm_email')
        return render(request, self.template_name, {'form':form})
     
        
        
        
class ConfirmEmailView(TemplateView):
    template_name = 'users/confirm_email.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ConfirmEmailForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ConfirmEmailForm(request.POST)
        if form.is_valid():
            email = request.session['confirm_email']
            user = User.objects.get(email=email)
            if user.confirmation_code == form.cleaned_data['code']:
                user.is_confirmed = True
                user.save()
                return redirect('login')
            else:
                messages.error(request, 'Неверный код подтверждения')
        return render(request, self.template_name, {'form':form}) # передаем ту же форму с ошибкой


class LoginView(TemplateView):
    template_name = 'users/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('bulletin_list')
        return render(request, self.template_name, {'form':form})
                
                
            
        
class LogoutView(TemplateView):
    template_name = 'users/logout.html'
    
    
