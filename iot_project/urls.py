from django.contrib import admin
from django.urls import path
from core.views import dashboard

urlpatterns = [
    path('admin/', admin.site.url_types),
    path('', dashboard, name='dashboard'),
]