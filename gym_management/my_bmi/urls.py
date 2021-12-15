from django.urls import path
from . import views

urlpatterns = [
    path('/Bmi', views.bmi, name="bmi"),


    # path('/nutrition', views.nutrition, name="nutrition"),
]
