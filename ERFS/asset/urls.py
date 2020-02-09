from django.conf.urls import url 
from django.urls import path
from . import views
app_name = "asset"
urlpatterns = [ 
    path('result/',views.result,name="result")
    
]