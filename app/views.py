from django.shortcuts import render
from django.core.mail import send_mail
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
        
        #send email
        send_mail(
            'Message from' + message_name,
            message,
            message_email,
            ['karemanaj.luis@yahoo.com'],
        )
        
        
        return render(request, 'login.html', {'message_name': message_name})
    else:
        return render(request, 'login.html', {})
        



def shop(request):
    products = Product.objects.all()
    context = {"products_Key":products}
    return render(request, 'shop.html', context)


def detailProduct(request, slug):
    productDetail = Product.objects.get(product_slug=slug)
    context = {"productDetail":productDetail}
    return render(request, 'detailProduct.html', context)
    