from django.contrib import admin
from .models import Health,WeightCat,BmiChart
# Register your models here.
class BmiAdmin(admin.ModelAdmin):
    list_filter = ("bmi","weight_category")
    list_display = ("bmi","weight_category","health_Risk")


admin.site.register(Health)
admin.site.register(WeightCat)
admin.site.register(BmiChart,BmiAdmin)