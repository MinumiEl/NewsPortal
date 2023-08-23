from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post, Category, Subscription


# @receiver(post_save, sender=Post)
# def post_created(instance, **kwargs):
#     print('Создана новость', instance)


@receiver(post_save, sender=Subscription)
def post_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category.name
    ).values_list('email', flat=True)

    subject = f'Новые новости {instance.category.name}'

    text_content = (
        f'Новость: {instance.name.title}\n'
        f'Категория: {instance.category.name}\n\n'
        f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новость: {instance.name.title}<br>'
        f'Категория: {instance.category.name}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
