from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView
from .models import Newsletter
from .forms import NewsletterForm
from django.urls import reverse_lazy
from users.models import User
from django.core.mail import send_mail
# Create your views here.

class NewsletterCreateViews(UserPassesTestMixin, CreateView):
    model = Newsletter
    template_name = 'newsletter/newsletter.html'
    context_object_name = 'Newsletter'
    form_class = NewsletterForm
    success_url = reverse_lazy('bulletin_list')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        users = User.objects.filter(is_subscribed_to_newsletter=True)
        for user in users:
            send_mail(
                form.cleaned_data['title'],
                form.cleaned_data['text'],
                'admin@django.com',
                [user.email],
                fail_silently=False
            )
        return super().form_valid(form)