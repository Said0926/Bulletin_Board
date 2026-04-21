from django.urls import path
from .views import NewsletterCreateViews

urlpatterns = [
    path('create/', NewsletterCreateViews.as_view(), name='newsletter_create')
]