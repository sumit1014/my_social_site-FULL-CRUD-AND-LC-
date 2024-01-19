from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from home.models import Contact
from blog.models import Post
from django.contrib.auth  import authenticate,  login, logout
from .forms import updateuserForm
#create functions
def home_page(request): 
    return render(request, "home/home_page.html")

def contact_page(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile_no=request.POST['mobile_no']
        msg =request.POST['msg']
        if len(name)<2 or len(email)<3 or len(mobile_no)<10 or len(msg)<4:
            messages.error(request, "Please,fill the contact form correctly!")
        else:
            contact=Contact(name=name, email=email, mobile_no=mobile_no, msg=msg)
            contact.save()
            messages.success(request, "Thank you for contacting us,Your message has been sent successfully")        
    return render(request, "home/contact_page.html")


def handlesignup(request):
    if request.method=="POST":
        # Get the post parameters
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # check for errorneous input
        if len(username)<8:
            messages.error(request," Your username must not be under 10 characters")
            return redirect("home:home")

        if not username.isalnum():
            messages.error(request," Username should be contain letters and numbers")
            return redirect("home:home")

        if (pass1!= pass2):
            messages.error(request," Passwords do not match")
            return redirect("home:home")
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " congratulations! Your account has been created  successfully")
        return redirect("home:home")
        
    else:
        return render(request, "home/signup_page.html")

   


def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home:home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home:home")
    else:
        return render(request, "home/login_page.html")

def handleLogout(request):
    logout(request)
    messages.success(request, "you are successfully logged out")
    return redirect("home:home")

def about_page(request): 
    return render(request, "home/about_page.html")

def profile_page(request): 
    return render(request, "home/profile_page.html")    

def edit_profile(request): 
    if request.method == "POST":
        form1 = updateuserForm(request.POST,instance=request.user)
        if form1.is_valid():
            form1.save()
            messages.success(request, "Your Blog has been updated successfully")
            return redirect("home:profile_page")
    else:
        form1 = updateuserForm(instance=request.user)
        return render(request, "home/edit_profile.html", {'form1': form1})