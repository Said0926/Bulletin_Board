from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import random

# наш собственный менеджер
class UserManager(BaseUserManager):
    # метод создание пользователей
    def create_user(self, email, password=None, **extra_fields):
        # обычная проверка
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email) # преврашает email в норм вид
        user = self.model(email=email, **extra_fields) # это и есть наш класс user
        user.set_password(password) # шифрует пароль
        user.save(using=self._db) #  сохроняет все в БД
        return user 
    # метод создания админки
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) # добавляет значение если они не были указаны явно 
        extra_fields.setdefault('is_superuser', True) # тоже самое что сверху
        extra_fields.setdefault('is_confirmed', True) # этот тоже
        return self.create_user(email, password, **extra_fields) # передает все в метод создание пользователей чтобы создать админку


class User(AbstractUser):
    username = None # для того чтобы можно было регистрироваться через email
    email = models.EmailField(unique=True)
    # для подтверждение почты
    confirmation_code = models.CharField(max_length=6, blank=True)
    is_confirmed = models.BooleanField(default=False)
    # подписка на рассылку
    is_subscribed_to_newsletter = models.BooleanField(default=True)
    
    objects = UserManager() # подлючаем наш менеджер (это все делается для того чтобы по email заходили)
    
    USERNAME_FIELD = 'email' #вход по email
    REQUIRED_FIELDS = []  # убираем username 
    
    # метод генерации верификационного кода
    def generate_code(self):
        self.confirmation_code = str(random.randint(100000, 999999))
        self.save()
    
    