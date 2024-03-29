"""mfresh_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from user.views import userLogin,userRegister,userCheckUname,userCheckPhone
from news.views import newsList,newsDetail
from product.views import productList,productDetail
from cart.views import cartDetailAdd,cartDetailList,cartDetailDelete,cartDetailUpdate

from user.models import MfUser

def handleHome(req):
    res=HttpResponse('<h1>welcome to mfresh!</h1><hr>')
    return res

urlpatterns = [
    path('',handleHome),
    path('user/login',userLogin),
    path('user/register',userRegister),
    path('user/check/uname',userCheckUname),
    path('user/check/phone',userCheckPhone),
    path('news/list',newsList),
    path('news/detail',newsDetail),
    path('product/list',productList),
    path('product/detail',productDetail)
]
