from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_page_day_night),
]