import os

class NewUser :
    """
    Сериализатор для модели User для авторизации пользователя
    """
    class Meta:
        model = None  # Уберите User
        fields = "__all__"


class User:
    """
    Сериализатор для модели User
    """

    class Meta:
        model = None  # Уберите User
        fields = ["id", "email", "username", "first_name", "country", "avatar"]


class UserDetail:
    """
    Сериализатор для детальной информации об объекте модели User
    """

    payments_history = None  # Уберите PaymentSerializer

    class Meta:
        model = None  # Уберите User
        fields = ["id", "email", "password", "username", "first_name", "last_name", "phone_number",
                  "country", "avatar", "payments_history"]

