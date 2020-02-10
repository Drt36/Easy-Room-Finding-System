from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from booking.models import Asset,Booking
# Create your tests here.
 
class DataTest(TestCase):
    def setUp(self):

        self.asset = Asset.objects.create(is_available=True,asset_Title="Room Available",  asset_Type="Room",asset_Price=15000,asset_purpose="Rent",asset_Location="Naxal",asset_Image="")

        self.user=User.objects.create(username="drt",first_name="Dharma Raj",last_name="Thanait",email="drt36@gmail.com",password="123");

        self.userprofile = UserProfile.objects.create(user_id=self.user.id, picture="", bio="I am Drt")

        self.book=Booking.objects.create(asset_id=self.asset.id,user_id=self.user.id,booking_Date="",booking_Status=True)


    def testAsset(self):
        a=Asset.objects.get(asset_Title="Room Available")
        self.assertEqual(a.asset_Title,"Room Available")

    def testAsset1(self):
        a1=Asset.objects.get(asset_Price=15000)
        self.assertEqual(a1.asset_Price,15000)


    def testUser(self):
        b=User.objects.get(first_name="Dharma Raj")
        self.assertEqual(b.first_name,"Dharma Raj")

    def testUserProfile(self):
        u=UserProfile.objects.get(bio="I am Drt")
        self.assertEqual(u.bio,"I am Drt")

    def testavailable(self):
        f=Asset.objects.get(is_available=True)
        self.assertEqual(f.is_available,True)

    def testbook(self):
        bk=Booking.objects.get(booking_Status=True)
        self.assertEqual(bk.booking_Status,True)