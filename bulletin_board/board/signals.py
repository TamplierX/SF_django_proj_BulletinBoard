from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from .models import Response


@receiver(post_save, sender=Response)
def create_response(instance, **kwargs):
    accept = True
    not_accept = False

    if instance.accepted == not_accept:

        email = instance.post.author.email

        subject = f'Вы получили отклик на Ваше объявление!'

        text_content = (
            f'К вашему объявлению {instance.post.title} написали отклик \n\n'
            f'Ссылка на отклик: http://127.0.0.1:8000{instance.get_absolute_url()}'
        )

        html_content = (
            f'К вашему объявлению {instance.post.title} написали отклик\n\n'
            f'Ссылка на отклик:: http://127.0.0.1:8000{instance.get_absolute_url()}'
        )

        msg = EmailMultiAlternatives(subject, text_content, 'testserver@test.ru', [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    elif instance.accepted == accept:

        email = instance.author.email

        subject = f'Ваш отклик был принят!'

        text_content = (
            f'Отклик к объявлению {instance.post.title} был принят \n\n'
            f'Ссылка на объявление: http://127.0.0.1:8000{instance.post.get_absolute_url()}'
        )

        html_content = (
            f'Отклик к объявлению {instance.post.title} был принят \n\n'
            f'Ссылка на объявление: http://127.0.0.1:8000{instance.post.get_absolute_url()}'
        )

        msg = EmailMultiAlternatives(subject, text_content, 'testserver@test.ru', [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
