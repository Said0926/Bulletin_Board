from django.db import models

# Create your models here.
class Newsletter(models.Model):
    title = models.CharField(max_length=255) # поле с названием
    text = models.TextField() # поле с текстом
    created_at = models.DateTimeField(auto_now_add=True) # поле со временем создания
    
    # метод отоброжения
    def __str__(self):
        return self.title

