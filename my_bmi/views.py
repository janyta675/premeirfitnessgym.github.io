from django.shortcuts import render
import requests
from .models import BmiChart
# Create your views here.

def bmi(request):
    bmi_result=0.00
    status=""
    my_bmi=BmiChart.objects.all()
    try:
        if request.method=="POST":
            num1=float(request.POST.get('height'))
            num2=float(request.POST.get('weight'))
            bmi=(num2/(num1**2))*5.05
            bmi_result=round(bmi,1)
            if bmi_result < 18.5:
                status="Under Weight!!"
            elif bmi_result >= 18.5 and bmi < 25.5:
                status="Normal(Healthy Weight)"
            elif bmi_result >= 25.5 and bmi_result < 30.5:
                status="Overweight!!"  
            elif bmi_result >= 30:
                status="Obese!!"
        return render(request,'bmi/bmi.html',{'status':status,'bmi_result':bmi_result,'my_bmi':my_bmi})
    except:
        return render(request, 'bmi/bmi.html', {'status':status,'bmi_result':bmi_result,'my_bmi':my_bmi})
