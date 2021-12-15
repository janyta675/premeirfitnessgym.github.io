from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
# from .models import ContactUs
# Create your views here.
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/contact.html', {"form": form,})
    else:
        form = ContactForm
        return render(request, 'forms/contact.html', {"form": form, })
