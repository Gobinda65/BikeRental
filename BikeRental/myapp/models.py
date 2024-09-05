from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile=models.CharField(max_length=10)

# Create your models here.
Fuel_Choice = (
    ('','Select'),
    ('Petrol','Petrol'),
    ('CNG', 'CNG'),
    ('EV','EV'),
)
ABS_Choice=(
    ('Yes','Yes'),
    ('No', 'No')
)
Break_choice=(
     ('Drum brakes','Drum brakes'),
    ('Disc brake', 'Disc brake'),
    ('Hydraulic disc brakes', 'Hydraulic disc brakes'),
)

class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=100,verbose_name='Student Name')
    smobile=models.CharField(max_length=10,verbose_name='Mobile')
    scity=models.CharField(max_length=50,verbose_name='City')

# class bike(models.Model):
#     b_no_plate=models.AutoField(primary_key=True)
#     ename=models.CharField(max_length=200,verbose_name='Employee_name')
#     emobile=models.CharField(max_length=100,verbose_name='Employee_ph_no')
#     ecity=models.CharField(max_length=50,verbose_name='Employee_city')
   
class binfo(models.Model):
    desc=models.CharField(max_length=400)
    price=models.DecimalField(max_length=10, max_digits=10, decimal_places=2)
    fuel_type=models.CharField(max_length=100)
    seating=models.CharField(max_length=10)
    bike_img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    abs_system=models.CharField(max_length=50)
    disk_break=models.CharField(max_length=50)
    reg_date=models.DateField(auto_now=False, auto_now_add=False)

class reg(models.Model):
    # e_id=models.AutoField(primary_key=True)
    firstname=models.CharField( max_length=100)
    lastname=models.CharField( max_length=200)
    phoneno=models.CharField( max_length=50)
    email=models.CharField( max_length=100)
    pickupcity=models.CharField(max_length=200)
    pickupdate=models.DateField(auto_now=False, auto_now_add=False)
    pickuptime=models.TimeField(auto_now=False, auto_now_add=False)
    dropdate=models.DateField(auto_now=False, auto_now_add=False)
    droptime=models.TimeField(auto_now=False, auto_now_add=False)
    location=models.CharField(max_length=50)
    vehicletype=models.CharField(max_length=200)

class Brand(models.Model):
    brand_id=models.AutoField(primary_key=True)
    brand_name=models.CharField(max_length=255,verbose_name='Name of Brand')
    about=models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name

class Bike(models.Model):
    bike_id=models.AutoField(primary_key=True)
    bike_title=models.CharField(max_length=255)
    bike_model=models.CharField(max_length=255)
    overview=models.TextField()
    p_p_day=models.CharField(max_length=5, verbose_name='Price per day')
    abs=models.CharField(max_length=30, choices=ABS_Choice, default='No')
    ftype=models.CharField(max_length=30, choices=Fuel_Choice, default="Select")
    b_break=models.CharField(max_length=30, choices=Break_choice, default='Drum brakes', verbose_name='Break Type')
    reg=models.CharField(max_length=15)
    b_img=models.ImageField(upload_to='bikes/')
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Name of Brand')


class Order(models.Model):
    payment_status=models.CharField(max_length=255)
    payment_id=models.CharField(max_length=255)

