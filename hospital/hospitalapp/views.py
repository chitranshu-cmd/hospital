from email import message
from django.shortcuts import render
from django.contrib.auth.models import User
from home.models import 



def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def Register(request):
    if request.method =="POST":
        first_name = request.POST['first name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password =request.POST['password']
        

        myuser = User.objects.create_user(first_name,last_name,Confirm_password)
        myuser.first_name =first_name
        myuser.last_name = last_name

        myuser.save()
        message.success(request,"created")
        return render('Register.html')

    return render(request,'Register.html')    

def signup(request):
    return render(request,'signup.html')    


    
        

# Create your views here.
