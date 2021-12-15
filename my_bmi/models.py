from django.db import models

# Create your models here.
from django.db import models
from django.db.models.lookups import GreaterThanOrEqual, IsNull, LessThanOrEqual

# Create your models here.
class Health(models.Model):
    health_Risk=models.TextField(max_length=1000)
    def __str__(self):
        return self.health_Risk
    
class WeightCat(models.Model):
    weight_category=models.CharField(max_length=500)
    def __str__(self):
        return self.weight_category
    
class BmiChart(models.Model):
    bmi=models.CharField(max_length=10)
    weight_category=models.ForeignKey(WeightCat,on_delete=models.SET_NULL,null=True)
    health_Risk=models.ForeignKey(Health,on_delete=models.SET_NULL, null=True)
   