from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm  , OrderForm
from .models import *
from django.core.mail import send_mail


# Create your views here.
def home(request):
    count = ViewCount.objects.get(id=1).a + 1
    ViewCount.objects.update(a=count)
    return render(request, 'index.html' , {})

def fa(request):
    return render(request, 'fa.html' , {})

def contact(request):
       


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
            send_mail(
                    'Contact',
                    'you have new contact',
                    'sarshary@gmail.com',
                    ['sarshary@gmail.com'],
                    fail_silently=False,
                    )
                
            return JsonResponse({
                'msg': 'Success'
                })


def order(request):
       


    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid() :
            form.save()
            send_mail(
                    'Order',
                    'you have new Order',
                    'sarshary@gmail.com',
                    ['sarshary@gmail.com'],
                    fail_silently=False,
                    )

                
            return JsonResponse({
                'msg': 'Success'
                })





