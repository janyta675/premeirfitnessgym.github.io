from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)

