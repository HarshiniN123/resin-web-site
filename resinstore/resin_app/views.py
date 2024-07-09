from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from .models import Orders
from django.core.mail import send_mail

# Create your views here.
# Front Page
def front(request):
    return render(request,'front.html')
    
# Home page
def home(request):
    return render(request, 'home.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

# Products Page
def products(request):
    return render(request, 'products.html')

# Orders Page
def orders(request):
    return render(request, 'orders.html')

# Discount Page    
def discount(request):
    return render(request, 'discount.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Framestand Page
def stand(request):
    return render(request, 'stand.html')

# Shipping Page
def shipping(request):
    return render(request, 'shipping.html')
 

# Database Connection for orders

def order(request):
    name = request.POST.get("name")
    phonenumber = request.POST.get("phonenumber")
    address = request.POST.get("address")
    email = request.POST.get("email")
    resin =request.POST.get("resin")
    wooden =request.POST.get("wooden")
    keychain=request.POST.get("keychain")
    productdesc=request.POST.get("productdesc")
    color=request.POST.get("color")
    c1 = Orders(name=name, phonenumber=phonenumber, address=address, email=email, resin=resin, wooden=wooden, keychain=keychain, productdesc=productdesc, color=color)
    c1.save()
    subject ='Welcome to Magical Resinarts site'
    messages='ThankYou for Shooping with us your order has been submited Keep shopping more!!!..'
    email_from ='harshini.naag@gmail.com'
    recipient_list=[email]
    send_mail(subject, messages, email_from, recipient_list)
    return render(request, 'orders.html')    
   



   