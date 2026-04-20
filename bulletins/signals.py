from .models import Response
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail

# какой сигнал слушаем / слушаем только модель Responce / уникальный id от двойного срабатывания 
@receiver(post_save, sender=Response, dispatch_uid='You_have_responce') # декоратор говорит 'эта функция слушает сигнал' 
# наша модель / конкретный объект который сохранился / True объект только что создан / остальные аргументы
def you_have_responce(sender, instance, created, **kwargs): 
    print('Signal fired...') # это для того чтобы понять сработал сигнал или нет 
    # если объект только что был создан отправляем письмо
    if created: 
        send_mail(
            'У вас новый отклик.',
            'Здравствуйте, на ваще объявление кто-то оставил отклик.',
            'admin@django.com',
            [instance.bulletin.author.email],
            fail_silently=False # если письмо не отправился будет ошибка так как False 
        )

# pre_save до сохранение объекта чтобы потом сравнить
@receiver(pre_save, sender=Response, dispatch_uid='track_is_accepted')
def track_is_accepted(sender, instance, **kwargs):
    # пробуем взять старые данне и добавить в instance
    try:
        old = Response.objects.get(pk=instance.pk)
        instance.__old_is_accepted = old.is_accepted # временная переменная 
    # если нет то ставим false
    except Response.DoesNotExist:
        instance.__old_is_accepted = False

# этот сигнал для того чтобы отправить фидбек с ответом на отклик
@receiver(post_save, sender=Response, dispatch_uid='send_feedback')
def send_feedback(sender, instance, created, **kwargs):
    # обычное условие и если True то отправляем письмо 
    if not created and instance.is_accepted == True and instance.__old_is_accepted == False:
        send_mail(
            'Вам пришел ответ.',
            'Здравствуйте, ваш отклик приняли',
            'admin@django.com',
            [instance.author.email],
            fail_silently=False
        )
