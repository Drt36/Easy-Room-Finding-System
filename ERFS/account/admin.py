from django.contrib import admin

# Register your models here.
# Registering All Model
from .models import UserProfile
from booking.models import Asset,Booking
admin.site.register(UserProfile)
admin.site.register(Asset)
admin.site.register(Booking)
