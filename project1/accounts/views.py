from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method=='POST':
        user_name=request.POST['UserName']
        email=request.POST['Email']
        Image=request.POST['Image']
        password=request.POST['Password']
        reenterpassword=request.POST['Reenter password']
        if password==reenterpassword:
            if User.objects.filter(user=user_name).exists():
                messages.info(request,"user taken")
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('accounts:register')
            else:                   
                user=User(user=user_name,email=email,password=password)
                user.save();
                messages.info(request,'user created')
        else:
            messages.info(request,"Password Incorrect")
            return redirect('accounts:register') 
        return redirect('/')                                       #here URL is same but by method identify GET or Post
    else:
        return render(request,'accounts/signup.html')
        
      
def userList(request):
    users=User.objects.all()
    return render(request,'accounts/users.html',{'users': users})
def login(request):
    if request.method =='POST':
        UserName=request.POST['UserName']
        if User.objects.filter(user=UserName).exists():
            m = User.objects.get(user=UserName)
            if m.password == request.POST['Password']:
                request.session['member_id'] = m.id
                messages.info(request,"You're logged in.")
                return redirect('/')
            else:
                messages.info(request," password didn't match.")
                return redirect('accounts:login')
        else:
            messages.info(request,"username not exist")
            return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html')
def logout(request):
    try:     
        del request.session['member_id']
        print("logout")        
    except KeyError:
        pass
    return redirect('accounts:login')
def update(request):
    pass

    