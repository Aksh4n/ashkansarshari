from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm 

# Create your views here.
def home(request):
    return render(request, 'index.html' , {})

def fa(request):
    return render(request, 'fa.html' , {})

def contact(request):
       


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
                
            return JsonResponse({
                'msg': 'Success'
                })






