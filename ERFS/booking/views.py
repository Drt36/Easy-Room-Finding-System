from django.shortcuts import render,redirect, get_object_or_404,reverse
from .models import Asset,Booking
from account.models import UserProfile
from .forms import UploadForm
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#method to upload assets and its details
@login_required(login_url='account:userlogin')
def upload(request):
    if request.method == "POST":
        form= UploadForm(request.POST, request.FILES)
        if form.is_valid(): #checks if every field is filled or not
            asset=form.save(commit=False)
            asset.user=request.user #stores logged in user id in the database asset
            asset.save() 
            messages.warning(request, 'Property Uploaded SuccessFully!!!.')  
        return redirect('booking:display') 
    else:      
        form= UploadForm()
        return render(request, "uploads/uploads.html", {"form": form}) #to display form 

#method to update the uploaded assets
@login_required(login_url='account:userlogin')
def update_asset(request, id=None):
    instance= get_object_or_404(Asset, id=id)
    if instance.user_id==request.user.id:
        form= UploadForm()
        if request.method == "POST":
            form= UploadForm(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                messages.warning(request, 'Property Updated SuccessFully!!!.')
            return redirect('booking:display')       
        return render(request, "uploads/uploads.html", {"form": form})
    else:
            messages.warning(request, 'You Can Not Update Others Property.')
            return redirect('booking:display')

#method to display uploaded assets and its details
def display(request):
    asset= Asset.objects.all()
    return render(request, "uploads/details.html",{"assets": asset})

#method to delete uploaded assets and its details
@login_required(login_url='account:userlogin')
def delete_asset(request, pk= None):
        asset= Asset.objects.get(pk=pk)
        if asset.user_id==request.user.id:
                asset.delete()
                messages.warning(request, 'Uploaded Property Deleted!!!.')
                return redirect('booking:soldasset')
        else:
            messages.warning(request, 'You Can Not Delete Others Property.')
            return redirect('booking:display')
    
#method to book assets        
@login_required(login_url='account:userlogin')
def book_asset(request,pk=None):
    asset = get_object_or_404(Asset, pk=pk)
    if asset.user_id==request.user.id:
        messages.warning(request, 'You Can Not Book Own Property.')
        return redirect('booking:display')

    else:
        if asset.is_available:
            asset.is_available= False
            asset.save()
            b=Booking(user_id=request.user.id)
            b.booking_Date=timezone.now()
            b.asset_id=pk
            b.booking_Status=True
            b.save()
            messages.success(request, 'Successfully Booked!!!.')
            return redirect('booking:bookedasset')
        else:
            asset.is_available = True
            asset.save()
        
#method to display booked assets 
@login_required(login_url='account:userlogin')
def bookedasset(request):
    booked= Booking.objects.filter(user_id=request.user.id)
    return render(request, 'uploads/booked.html', {"booked":booked})

#method to display the assets uploaded by the user in user profile
@login_required(login_url='account:userlogin')
def soldasset(request):
        sold=Asset.objects.filter(user_id=request.user.id)
        return render(request, 'uploads/sold.html', {"sold":sold})


@login_required(login_url='account:userlogin')
def delete_booking(request,pk=None):
    b=Booking.objects.get(pk=pk)
    b.delete()
    b.asset.is_available =True
    b.asset.save()
    messages.error(request, 'Booked Property Deleted!!!')
    return redirect('booking:bookedasset')    


   