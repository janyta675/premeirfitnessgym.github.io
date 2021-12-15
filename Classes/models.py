from django.db import models
# Create your models here.


class Trainer(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    occupation = models.CharField(max_length=200)

    def get_full_name(self):
        return f"{self.firstname} {self.lastname} {self.occupation}"

    def __str__(self):
        return self.get_full_name()


class Classes(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    details = models.CharField(max_length=560)
