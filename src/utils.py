import os
from django.contrib.auth.models import Group

def get_queryset_for_owner(user, queryset):
    try:
        if user.is_superuser or user.groups.get(name="Moderators"):
            return queryset.order_by("id")
    except Group.DoesNotExist:
        return queryset.filter(owner=user).order_by("id")

# Удалены функции, связанные со stripe
# def create_product(instance):
#     """
#     Создание продукта
#     """
#     instance_name = f"Оплата курса {instance.course.name}" if instance.course \
#         else f"Оплата урока {instance.lesson.name}"
#     return Product.create(name=instance_name)

# def create_price(instance):
#     """
#     Создание цены
#     """
#     return Price.create(
#         currency="rub",
#         unit_amount=instance.amount * 100,
#         product=create_product(instance).get("id"),
#     )

# def create_session(price):
#     """
#     Создание сессии на оплату
#     """
#     session = checkout.Session.create(
#         success_url="https://127.0.0.1:8000/payments/",
#         line_items=[{"price": price.get("id"), "quantity": 1}],
#         mode="payment",
#     )
#     return session.get("id"), session.get("url")

# def check_session_status(session_id):
#     """
#     Уточнение статуса сессии
#     """
#     return checkout.Session.retrieve(session_id).get("payment_status")
