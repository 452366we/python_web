from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def userLogin(req):
    n=req.GET.get('uname','guest')
    p=req.GET.get('upwd','')
    res=HttpResponse('<h3>user login</h3>')
    return res

def userRegister(req):
    res=HttpResponse('<h3>user register</h3>')
    return res