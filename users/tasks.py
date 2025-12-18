import os

def block_inactive_users():
    """
    Блокирует пользователя, если он не заходил более месяца
    """
    # today = timezone.now()  # Уберите это, если не используете timezone

    # users = User.objects.filter(is_active=True)  # Уберите это, если не используете User
    # for user in users:
    #     if user.last_login and (today - user.last_login).days >= 30:
    #         user.is_active = False
    #         user.save()
    #         print(f"{user} - заблокирован")
