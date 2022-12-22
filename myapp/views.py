

from django.http.response import HttpResponse
from django.shortcuts import render
from product.models import Category, Product, Imagess, Comment


# Create your views here.
def index(request, ):
   category=Category.objects.all()
   sliderData=Product.objects.all()[:4]
   mostRead=Product.objects.all()[:4]
   recentlyAdded=Product.objects.all().order_by('-id')[:4]
   popularBooks=Product.objects.all().order_by('?')[:4]

   context={'category':category,
            'sliderData':sliderData,
            'mostRead':mostRead,
            'recentlyAdded':recentlyAdded,
            'popularBooks':popularBooks}
   return render(request,'index.html',context)


def category_products(request,id,slug):

   category=Category.objects.all()
   selectedCategory=Category.objects.filter(pk=id)
   products=Product.objects.filter(category_id=id)
   context={'selectedCategory':selectedCategory,

            'products':products,
            'category':category}
   return render(request,'category_products.html',context)



def product_detail(request,id,slug):
   comment = Comment.objects.filter(product_id=id,status='True')
   category=Category.objects.all()
   images=Imagess.objects.filter(product_id=id)
   products=Product.objects.filter(pk=id)
   context={
            'comments': comment,
            'products':products,
            'category':category,
            'images':images}
   return render(request,'product_detail.html',context)
