from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import math
from .models import MfNews

def newsList(req):
    pageNum=req.GET.get('pageNum',1)
    pageNum=int(pageNum)
    pageSize=10
    totalRecord=MfNews.objects.count()
    pageCount=math.ceil( totalRecord/pageSize )
    r=MfNews.objects.order_by('-pubtime').values('nid','title','pubtime')
    start=pageSize*(pageNum-1)
    end=pageNum*pageSize
    data=list(r[start:end])
    print(data,type(data))
    res=JsonResponse({
        'totalRecord':totalRecord,
        'pageSize':pageSize,
        'pageCount':pageCount,
        'pageNum':pageNum,
        'data':data
    })
    res['Access-Control-Allow-Origin']='*'
    return res

def newsDetail(req):
    nid=req.GET.get('nid')
    r=MfNews.objects.filter(nid=nid).values()
    if(len(r)>0):
        n=r[0]
        res=JsonResponse({
            'nid':n['nid'],
            'title':n['title'],
            'pubtime':n['pubtime'],
            'content':n['content']
        })
    res['Access-Control-Allow-Origin']='*'
    return res