from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User 

from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.models import Games , Contact
# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("this is home page")

def about(request):
    return render(request,"about.html")
    # return HttpResponse("this is about page")


#Contact us module.
def contact(request):
    if request.method=="POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        comment= request.POST['comment']
        contact = Contact(fname=fname,lname=lname,email=email,comment=comment)
        contact.save()
    return render(request,"contact.html")
    # return HttpResponse("this is contact page")




@login_required(login_url='login')
def games(request):
    if request.method=='POST':
        gameDate=request.POST['gameDate']
        gameSlot=request.POST['gameSlot']
        teamname= request.POST['teamname']
        player1= request.POST['player1']
        player2= request.POST['player2']
        player3= request.POST['player3']
        player4= request.POST['player4']
        phoneno=request.POST['phoneno']
        games = Games(gameDate=gameDate,gameSlot=gameSlot,teamname=teamname, player1=player1, player2=player2, player3=player3, player4=player4, phoneno=phoneno, date=datetime.today())
        print(games)
        games.save()
        messages.success(request, "Registered Successfully for match...")
    return render(request,"games.html")

    # return HttpResponse("this is games page")
def register(request):
    if request.user.is_authenticated:
        return redirect('games')
    else:
        if request.method=='POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_name = request.POST['user_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            if password1==password2:
                if User.objects.filter(username=user_name).exists():
                    messages.info(request,'user name taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email ID taken')
                else:
                    user = User.objects.create_user(user_name,password=password1 , email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    print('user created')
                    
            else:
                messages.info(request,'password not matching')
                return redirect('register')

            return redirect('/')
        else:    
            return render(request,"register.html")

    

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('games')
    else:
        if request.method=='POST':
            username = request.POST.get('user_name')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request,username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('games')
                
            else:
                messages.info(request,'Invalid Credentials')
        return render(request ,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
            

    