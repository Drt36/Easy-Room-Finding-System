from django.shortcuts import render,redirect
from booking.models import Asset
from django.contrib import messages
from django.db.models import Q
from django import template



# Create your views here.



def result(request):
    query =" "
    context = {}
    if request.GET:
        query = request.GET['q']
    asset = get_data_queryset(query)
    context['asset'] = asset
    
    return render(request, "result.html", context)  

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        assets = Asset.objects.filter(Q(asset_Title__startswith=q) | Q(asset_Title__icontains=q))

        for asset in assets:
            queryset.append(asset)
    return list(set(queryset))            



