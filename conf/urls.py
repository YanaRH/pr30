import os
from django.contrib import admin
from django.urls import path, include

# Определение маршрутов URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(("users.urls", 'users'), namespace="users")),  # Добавлен префикс 'users/'
    path('materials/', include(("materials.urls", 'materials'), namespace="materials")),  # Добавлен префикс 'materials/'
]

