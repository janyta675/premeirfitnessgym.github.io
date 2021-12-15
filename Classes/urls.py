from django.urls import path
from . import views

urlpatterns = [
    path('/Classes', views.classes, name="classes"),
]
