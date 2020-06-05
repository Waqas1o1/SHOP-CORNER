from django.shortcuts import render,HttpResponse
from .models import Product
# Create your views here.
def home(request):
    pdt = Product.objects.all()
    pdt_dict = {'products': pdt}
    return render(request,'Home/home.html',pdt_dict)
def Index(request):
    return HttpResponse('<small>Hey there is you</small>')
