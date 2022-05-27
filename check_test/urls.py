"""check_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.billing, name='billing'),
    path('history/', views.history, name='history'),
    path('check/<int:id>/', views.check, name='check'),
    path('check_list_recipient/', views.check_list_recipient, name='check_list_recipient'),
    path('check_list_sender/', views.check_list_sender, name='check_list_sender'),
    path('source/history/', views.source_history, name='source_history'),
]
