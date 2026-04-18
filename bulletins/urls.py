from django.urls import path
from .views import (
    BulletinListView,
    BulletinDetailView,
    BulletinCreateView,
    BulletinEditView,
    BulletinDeleteView,
    MyResponsesView,
    ResponseAcceptView,
    ResponseDeleteView,
    
)

urlpatterns = [
    path('', BulletinListView.as_view(), name='bulletin_list'),
    path('bulletins/create/', BulletinCreateView.as_view(), name='bulletin_create'),
    path('bulletins/<int:pk>/', BulletinDetailView.as_view(), name='bulletin_detail'),
    path('bulletins/<int:pk>/edit/', BulletinEditView.as_view(), name='bulletin_edit'),
    path('bulletins/<int:pk>/delete/', BulletinDeleteView.as_view(), name='bulletin_delete'),
    path('my-responses/', MyResponsesView.as_view(), name='my_responses'),
    path('response/<int:pk>/accept', ResponseAcceptView.as_view(), name='response_accept'),
    path('response/<int:pk>/delete', ResponseDeleteView.as_view(), name='response_delete'),
]