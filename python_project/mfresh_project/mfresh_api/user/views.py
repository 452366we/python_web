from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import MfUser

def userLogin(req):
    unameOrPhone=req.GET.get('unameOrPhone')
    upwd=req.GET.get('upwd')
    r=MfUser.objects.filter(uname=unameOrPhone,upwd=upwd) or MfUser.objects.filter(phone=unameOrPhone,upwd=upwd)
    if(len(r)>0):
        u=r[0]
        res=JsonResponse({
            'code':200,
            'uid':u.uid,
            'uname':u.uname,
            'phone':u.phone
        })
    else:
        res=JsonResponse({
            'code':400
        })
    res['Access-Control-Allow-Origin']='*'
    return res

def userRegister(req):
    uname=req.POST.get('uname')
    upwd=req.POST.get('upwd')
    phone=req.POST.get('phone')
    u=MfUser.objects.create(uname=uname,upwd=upwd,phone=phone)
    if(u): 
        res=JsonResponse({
            'code':200,
            'uid':u.uid,
            'uname':u.uname,
            'phone':u.phone
        })
    else:
        res=JsonResponse({
            'code':500
        })
    res['Access-Control-Allow-Origin']='*'
    return res

def userCheckUname(req):
    uname=req.GET.get('uname')
    r=MfUser.objects.filter(uname=uname).values()
    if(len(r)>0):
        res=JsonResponse({
            'code':1,
            'msg':'exist'
        })
    else:
        res=JsonResponse({
            'code':2,
            'msg':'non-exist'
        })
    res['Access-Control-Allow-Origin']='*'
    return res

def userCheckPhone(req):
    phone=req.GET.get('phone')
    r=MfUser.objects.filter(phone=phone).values()
    if(len(r)>0):
        res=JsonResponse({
            'code':1,
            'msg':'exist'
        })
    else:
        res=JsonResponse({
            'code':2,
            'msg':'non-exist'
        })
    res['Access-Control-Allow-Origin']='*'
    return res