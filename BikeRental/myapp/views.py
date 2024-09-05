import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . forms import MyStdRegFrm,empregfrm,UserRegFrm,UserlogFrm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return render(request,'myapp/about.html')
def services(request):
    return render(request,'myapp/services.html')
def review(request):
    return render(request,'myapp/review.html')
def contactus(request):
    return render(request, 'myapp/contactus.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        User=authenticate(request, username=username,password=password)
        if User is not None:
            User.save()
            return redirect('home-page')
        else:
            return HttpResponse("user name & password are not to match ")
    return render(request, 'myapp/login.html')
def singup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conpassword=request.POST.get('confrompassword')
        if password!=conpassword:
            return HttpResponse("password and confrompasswod are not valid")
        else:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            return redirect('login-page')
    return render(request,'myapp/singup.html')
def cart(request):
#     if request.user.is_authenticated:
#         product = Product.objects.get(id=product_id)
#         cart_item, created = CartItem.objects.get_or_create(product=product, 
#                                                         user=request.user)
#         cart_item.quantity += 1
#         cart_item.save()
#         return redirect('/cart')
#     else:
#         return redirect('/login')
    return render(request,'myapp/cart.html')
# def rent(request):
#     if request.POST:
#         frm=empregfrm(data=request.POST)
#         if frm.is_valid():
#             try:
#                 frm.save()
#             except Exception as e:
#                 print(e)
#     else:
#         frm=empregfrm()
#     context={'frm':frm}
#     return render(request,'myapp/rent.html',context)


def userReg(request):
    if request.POST:
        frm=UserRegFrm(data=request.POST)
        if frm.is_valid():
            try:
                frm.save()
                messages.success(request,'Registration is succesfull')
                
            except Exception as e:
                messages.error(request,'Registration is unsuccesfull')
                
    else:
        frm=UserRegFrm()
    context={'frm':frm}
    return render(request,'myapp/userReg.html',context)


def userLogin(request):
    frm=UserlogFrm()
    context={'frm':frm}
    return render(request, 'myapp/userLogin.html',context)

def reg(request):
    if request.POST:
        frm=MyStdRegFrm(data=request.POST)
        if frm.is_valid():
            try:
                frm.save()
                messages.success(request,'Student details save Succesfully')
            except Exception as e:
                 messages.error(request,'Student details not save Succesfully')

    else:
        frm=MyStdRegFrm()
    context={'frm':frm}
    return render(request,'myapp/reg.html',context)

def readmore(request):
    return render(request,'myapp/readmore.html')

def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST["amount"])*100 #Amount in Paise
        address=request.POST['address']
        client=razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data ={
            "amount":amount,
            "currency":"INR",
            "receipt":"order_receipt",
            "notes":{
                "email": "user_email@example.com"
            },
        }

        order = client.order.create(data=payment_data)
        
        #Include key,name,description and image in the JSON respons
        response_data={
            "id":order["id"],
            "amount":order["amount"],
            "currency":order["amount"],
            "key":settings.RAZORPAY_API_KEY,
            "name":"My Project",
            "description":"Payment for your Poruduct",
            "image":"hhtps://ypurwebsite.com/logo.png",
        }

        # cart_items=CartItem.objects.filters(user=request)
        

def payment_success(request):
    return render(request,"myapp/home.html")


