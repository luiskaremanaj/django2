from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
# Create your views here.



def index(request):
    return render(request, 'index.html', {})

def login(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_phone = request.POST['message-phone']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        if message_name != '' and message_phone != '' and message_email != '' and message != '':
            FormContact(
                formContact_name=message_name,
                formContact_phone=message_phone,
                formContact_email=message_email,
                formContact_text=message,
            ).save()
            messages.success(request, 'Thank You For Contacting Us')
        else:
            messages.error(request, 'Please Fill All The Fields')
    return render(request, 'login.html',)

        



def shop(request):
    products = Product.objects.all()
    context = {"products_Key":products}
    return render(request, 'shop.html', context)


def detailProduct(request, slug):
    productDetail = Product.objects.get(product_slug=slug)
    context = {"productDetail":productDetail}
    return render(request, 'detailProduct.html', context)
    