from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def productList(req):
    res=JsonResponse({
        
    })
    res['Access-Control-Allow-Origin']='*'
    return res

def productDetail(req):
    res=JsonResponse({
        
    })
    res['Access-Control-Allow-Origin']='*'
    return res
