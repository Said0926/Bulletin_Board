from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.TextChoices):
    TANKS      = 'tanks',      'Танки'
    HEALERS    = 'healers',    'Хилы'
    DD         = 'dd',         'ДД'
    TRADERS    = 'traders',    'Торговцы'
    GUILDMASTERS = 'guildmasters', 'Гилдмастеры'
    QUESTGIVERS  = 'questgivers',  'Квестгиверы'
    BLACKSMITHS  = 'blacksmiths',  'Кузнецы'
    TANNERS    = 'tanners',    'Кожевники'
    POTIONERS  = 'potioners',  'Зельевары'
    SPELLMASTERS = 'spellmasters', 'Мастера заклинаний'
    
class Bulletin(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # поля автор внешний ключ 
    title = models.CharField(max_length=255) # поле название 
    text = RichTextUploadingField() # самое интересеное, это описание где будет текст, видео и фото
    category = models.CharField(max_length=20, choices=Category.choices) # поле категория которая выбирается сверху
    created_at = models.DateTimeField(auto_now_add=True) # поле время создание автоматом заполняется
    
    # метод отображение
    def __str__(self):
        return self.title
    
class Response(models.Model):
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE, related_name='responce') # поле название объявления, внешний ключ 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # поле автор тоже внешний ключ 
    text = models.TextField() # поле текст 
    is_accepted = models.BooleanField(default=False) # поле принято или нет по умолчанию не принято 
    created_at = models.DateTimeField(auto_now_add=True) # поле время создание автоматом заполняется
    
    