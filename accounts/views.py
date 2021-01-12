from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
from contacts.models import Contact


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(req,username=username,password=password)

        if user is not None:
            auth.login(req,user)
            return redirect('dashboard')
        else:
            messages.error(req,"invalid user or password")
            return redirect('login')






    return render(req,'accounts/login.html')

def register(req):
#
    if req.method == 'POST':
        firstname = req.POST['first_name']
        lastname = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password != password2:
            messages.add_message(req,messages.ERROR,"Passwords Doesn't match")
            return redirect('register')
        else:
            emailc = User.objects.filter(email=email)
            if emailc.exists() :
                messages.add_message(req,messages.ERROR,"Email is already Taken")
                return redirect('register')
            else:
                usernamec = User.objects.filter(username=username)
                if usernamec.exists():
                    messages.add_message(req,messages.ERROR,"User is already Taken")
                    return redirect('register')
                else:
                    newUser = User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
                    newUser.save()
                    messages.add_message(req, messages.INFO, "you can login now")
                    return redirect('index')






    else:
        return render(req,'accounts/register.html')

def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.add_message(req,messages.SUCCESS,"you logged out successfully")
        return redirect('index')



    return redirect('index')

def dashboard(req):
    user_contact = Contact.objects.all().filter(user_id=req.user.id)




    return render(req,'accounts/dashboard.html',{
        'listings':user_contact
    })