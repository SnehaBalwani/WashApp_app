from django.views.generic import ListView
from django.shortcuts import render
from django.contrib import messages
from .models import Customer

def home(request):
    return render(request, 'customer/home.html')
def register(request):
    if request.method == "POST":
        FirstName = request.POST.get('FirstName', '')
        LastName = request.POST.get('LastName', '')
        EmailId = request.POST.get('EmailId', '')
        PhoneNo = request.POST.get('PhoneNo', '')
        address = request.POST.get('address', '')
        Password = request.POST.get('Password','')

        customer = Customer(FirstName=FirstName, LastName=LastName,address=address, EmailId=EmailId, PhoneNo=PhoneNo, Password=Password )
        customer.save()
        a = Customer.FirstName
        messages.success(request, f'Account created for {a}!')
    return render(request, 'customer/register.html')

def login(request):

    if request.method == 'POST':
        FirstName=request.POST.get('FirstName', '')
        Password=request.POST.get('Password', '')
        customer = Customer.objects.filter(FirstName=FirstName, Password=Password)
        if customer is not None:
            return render(request, 'customer-home')
        else:
            return render(request, 'customer/login.html')
    return render(request, 'customer/login.html')
