from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from  . import views
app_name="account"
urlpatterns = [ 
 path('',views.sucess,name="sucess"),  
 path('userregister/',views.userregister,name="userregister"),
 path('userlogin/',views.userlogin,name="userlogin"),
 path('sucess/',views.sucess,name="sucess"),
 path('userlogout/',views.userlogout,name="userlogout"),
 path('uploadprofile/',views.uploadprofile,name="uploadprofile"),
 path('viewprofile/',views.viewprofile,name="viewprofile"),
]