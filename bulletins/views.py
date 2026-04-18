from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View
from .models import Bulletin, Response
from .forms import ResponseForm, BulletinForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

# Create your views here.
class BulletinListView(ListView):
    model = Bulletin # модель в бд
    template_name = 'bulletins/bulletin_list.html' # какой шаблон 
    context_object_name = 'bulletins'  # имя переменной в шаблоне
    ordering = ['-created_at']         # сначала новые
    
    
class BulletinDetailView(DetailView):
    model = Bulletin
    template_name = 'bulletins/bulletin_detail.html' 
    context_object_name = 'bulletin'

    # передаём форму отклика в шаблон (добавляем форму в шаблон чтобы на странице было видно)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResponseForm()
        return context

    # обрабатываем отправку отклика
    def post(self, request, *args, **kwargs):
        bulletin = self.get_object() # получаем текущее объявление
        form = ResponseForm(request.POST) # получаем форму (все что ввел пользователь)
        # проверка формы
        if form.is_valid():
            response = form.save(commit=False) # создаем объект, но не сохраняем в бд (потому что нам еще нужны author и bulletin)
            response.author = request.user # из запроса получаем автора 
            response.bulletin = bulletin # также получаем bulletin
            response.save() # вот теперь сохроняем все в бд
            messages.success(request, 'Ваш отклик успешно отправлен')
            return redirect('bulletin_list') # перенаправляем пользователя 
        return self.get(request, *args, **kwargs) # если форма плохая то заново показываем страницу

    
class BulletinCreateView(LoginRequiredMixin, CreateView):
    model = Bulletin
    template_name = 'bulletins/bulletin_create.html'
    form_class = BulletinForm
    success_url = reverse_lazy('bulletin_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user # добавляем автора
        return super().form_valid(form) 
    
    
class BulletinEditView(LoginRequiredMixin, UpdateView):
    model = Bulletin
    template_name = 'bulletins/bulletin_edit.html'
    form_class = BulletinForm
    success_url = reverse_lazy('bulletin_list')
    
    # можно редактировать только свое объявление
    def dispatch(self, request, *args, **kwargs):
        bulletin = self.get_object()
        if bulletin.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    
    
    
class BulletinDeleteView(LoginRequiredMixin, DeleteView):
    model = Bulletin
    template_name = 'bulletins/bulletin_delete.html'
    success_url = reverse_lazy('bulletin_list')
    
    
    # можно удалять только свое объявление
    def dispatch(self, request, *args, **kwargs):
        bulletin = self.get_object()
        if bulletin.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    
    
class MyResponsesView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'bulletins/my_responses.html'
    context_object_name = 'responses'  # имя переменной в шаблоне
    
    def get_queryset(self):        
        responses = Response.objects.filter(bulletin__author=self.request.user)  # только отклики на мои объявления
        bulletin_id = self.request.GET.get('bulletin')  # получаем id объявления из GET параметра
        if bulletin_id:
            responses = responses.filter(bulletin_id=bulletin_id)  # фильтруем по конкретному объявлению
        return responses
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bulletins'] = Bulletin.objects.filter(author=self.request.user)  # все мои объявления для фильтра
        return context
    
class ResponseAcceptView(LoginRequiredMixin, View):
    model = Response

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        response = get_object_or_404(Response, pk=pk)
        if response.bulletin.author != self.request.user:
            raise PermissionDenied
        response.is_accepted = True
        response.save()
        return redirect('my_responses')



class ResponseDeleteView(LoginRequiredMixin, DeleteView):
    model = Response
    success_url = reverse_lazy('my_responses')
    
    def dispatch(self, request, *args, **kwargs):
        response = self.get_object()
        if response.bulletin.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)