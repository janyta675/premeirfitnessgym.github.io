from django.contrib import admin
from .models import Trainer, Classes
# Register your models here.


class TrainerAdmin(admin.ModelAdmin):
    list_filter = ("firstname", "lastname")
    list_display = ("firstname", "lastname", "email", "occupation")


class ClassesAdmin(admin.ModelAdmin):
    list_filter = ("name", "trainer")
    list_display = ("name", "trainer")


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Classes, ClassesAdmin)
