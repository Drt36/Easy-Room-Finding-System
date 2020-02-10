from django.conf.urls import url 
from django.urls import path
from . import views #Importing views 

app_name = "asset"

urlpatterns = [ 

    path('result/',views.result,name="result") #Defining the path for search result
    
]