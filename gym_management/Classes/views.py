from django.shortcuts import render
from .models import Classes
# Create your views here.
def classes(request):
    class_list=Classes.objects.all()
    return render(request, 'classes/classes.html', {"classes": class_list})
