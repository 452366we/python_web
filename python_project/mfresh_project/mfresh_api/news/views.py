from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def newsList(req):
    res=JsonResponse({
        
    })
    res['Access-Control-Allow-Origin']='*'
    return res

def newsDetail(req):
    res=JsonResponse({
        
    })
    res['Access-Control-Allow-Origin']='*'
    return res