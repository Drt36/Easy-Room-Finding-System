from django.shortcuts import render,redirect #Importing render and redirect
from booking.models import Asset #Importing Asset models from booking app
from django.contrib import messages #Importing message for search feature
from django.db.models import Q #Importing Q

#Function to pass results in 'result.html'
def result(request):

    query =" "
    context = {}

    if request.GET:
        query = request.GET['q']

    asset = get_data_queryset(query)
    context['asset'] = asset
    
    return render(request, "result.html", context)  

#Function to check value for search.
def get_data_queryset(query=None):

    queryset = []
    queries = query.split(" ")

    for q in queries:
        assets = Asset.objects.filter(Q(asset_Title__startswith=q) | Q(asset_Title__icontains=q)) #Checks the first letter of word and whole word

        for asset in assets:
            queryset.append(asset)

    return list(set(queryset))            



