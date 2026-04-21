from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, ConfirmEmailView, LoginView, SubscribeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmEmailView.as_view(), name='confirm_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe')
]