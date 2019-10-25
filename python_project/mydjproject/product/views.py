from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

def productList(req):
    data={'ename':'dingding','isMarried':True}
    res=JsonResponse(data)
    res['Access-Control-Allow-Origin']='*'
    return res

def productDetail(req,pid):
    print(pid,type(pid))
    res=HttpResponse('<h2>product detail</h2>')
    return res