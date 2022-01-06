from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/blog', views.blog, name="blog"),
    path('/blog/<slug:slug>', views.blog_details, name="blog-details"),
]
