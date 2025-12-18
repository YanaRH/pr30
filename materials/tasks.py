import os
from django.core.mail import send_mail
from .models import Course, Subscription

def send_message_about_course_update(pk):
    """
    Отправка подписавшимся пользователям уведомления об обновлении
    """
    course = Course.objects.get(pk=pk)
    message = f"Курс {course} обновлен"
    subscriptions = Subscription.objects.filter(course=course, is_active=True)

    if subscriptions.exists():
        users = [subscription.owner for subscription in subscriptions]
        users_emails = [user.email for user in users]

        email_host_user = os.getenv("EMAIL_HOST_USER", "default_email@example.com")

        send_mail("Новые материалы", message, email_host_user, users_emails)





