from django.shortcuts import render
from .models import Home,Testimonial,Product_details,About
# Create your views here.


def home(request):
    data=Home.objects.order_by("-id").first()
    testimonial=Testimonial.objects.all()
    context={
        "data":data,
        'testimonial':testimonial,
    }
    return render(request, 'home.html',context)


def Products(request):
    data=Product_details.objects.last()
    return render(request,'product.html',{"data":data})


def about(request):
    data=About.objects.last()
    context={
        "data":data,
    }
    return render(request,'about.html',context)


def Contact(request):
    return render(request,'contact.html')


def partnerships(request):
    return render(request,'partners.html')