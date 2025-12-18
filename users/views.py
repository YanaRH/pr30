import os
import logging

from django.utils import timezone
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response

from materials.models import Payment
from src.utils import get_queryset_for_owner

from users.models import User
from users.permissions import IsCurrentUser , IsModerator, IsOwner


# Create your views here.
class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    Дженерик для отображения списка и создания нового объекта User:
    """
    queryset = User.objects.all()
    serializer_class = None  # Уберите UserSerializer

    def get_permissions(self):
        """
        Выдача разрешений в зависимости от статуса пользователя
        """
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_serializer_class(self):
        """
        Подбор сериализатора в зависимости от действий на странице
        """
        if self.request.method == "POST":
            return None  # Уберите NewUser  Serializer
        return None  # Уберите UserSerializer

    def perform_create(self, serializer):
        """
        Сохранение пароля и активация учетной записи при создании
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Дженерик для просмотра, редактирования и удаления объекта User:
    """
    queryset = User.objects.all()
    serializer_class = None  # Уберите UserDetailSerializer

    def get_serializer_class(self):
        """
        Подбор сериализатора в зависимости от статуса пользователя
        """
        if self.request.user.is_superuser or self.request.user == self.get_object():
            return None  # Уберите UserDetailSerializer
        return None  # Уберите UserSerializer

    def get_permissions(self):
        """
        Выдача разрешений в зависимости от статуса пользователя
        """
        if self.request.method in ["PATCH", "PUT"]:
            self.permission_classes = [IsCurrentUser  | IsModerator | IsAdminUser ]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsCurrentUser  | IsAdminUser ]
        return super().get_permissions()


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    """
    Дженерик для отображения списка и создания нового объекта Payment:
    """
    queryset = Payment.objects.all()
    serializer_class = None  # Уберите PaymentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["payment_date"]
    filterset_fields = ["course", "lesson", "payment_method"]

    def get_queryset(self):
        """
        Подбор списка объектов в зависимости от статуса пользователя
        """
        return get_queryset_for_owner(self.request.user, self.queryset)

    def perform_create(self, serializer):
        """
        Сохранение владельца при создании объекта
        """
        payment = serializer.save()
        payment.owner = self.request.user
        payment.save()  # Удалены вызовы функций создания цены и сессии


class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Дженерик для просмотра, редактирования и удаления объекта Payment:
    """
    queryset = Payment.objects.all()
    serializer_class = None  # Уберите PaymentSerializer

    def get_permissions(self):
        """
        Выдача разрешений в зависимости от статуса пользователя
        """
        if self.request.method == "GET":
            self.permission_classes = [IsOwner | IsModerator | IsAdminUser ]
        elif self.request.method in ["PATCH", "PUT", "DELETE"]:
            self.permission_classes = [IsModerator | IsAdminUser ]
        return super().get_permissions()

    def get_object(self):
        """
        Уточнение статуса для неоплаченного платежа при обращении к объекту
        """
        payment = super().get_object()
        # Удален вызов функции проверки статуса сессии
        return payment


class MyToken(generics.GenericAPIView):  # Замените TokenObtainPairView на GenericAPIView
    """
    Представление для получения токенов авторизации
    """
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Заполнение поля last_login при получении токенов авторизации
        """
        # Здесь нужно будет реализовать логику получения токенов
        user = User.objects.get(email=request.data["email"])
        user.last_login = timezone.now()
        user.save()
        return Response({"message": "Token obtained successfully"})  # Замените на вашу логику
