"""ProgramlamaOdevRepo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from ProgramlamaOdevRepo import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from myapp import views

# http://127.0.0.1:8000/  =>homepage
# http://127.0.0.1:8000/index =>homepage
# http://127.0.0.1:8000/blogs =>blogs
# http://127.0.0.1:8000/blogs/3 =>blog-details


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
    path('', include('myapp.urls')),
    path('product/',include('product.urls')),
    path('category/<int:id>/<slug:slug>',views.category_products,name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail')
]

if settings.DEBUG:# new
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)