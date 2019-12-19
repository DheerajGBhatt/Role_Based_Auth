from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.views import *
from django.shortcuts import redirect
from Users.forms.loginform import UserForm
from Users.forms.user_role import UserRoleForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from Roles.models import *
from Users.models import *
from operations import *
# Create your views here.

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

def register(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')            
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    form.operation = operations(request.user.id)
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def home(request):
    if request.user.is_authenticated:
        res=request.user
        print(request.user.id)
        res.operation = operations(request.user.id)   
        return render(request = request,
                    template_name = "home.html",
                    context={"form":res})
    else:
        form = AuthenticationForm()
        return redirect('login')

def create(request):  
    if request.user.is_authenticated:   
        if request.method == "POST":  
            user = UserForm(request.POST) 
            user.save() 
            if user.is_valid():  
              try:  
                user.save()
                messages.info(request, "user created")
              except:  
                     messages.error(request, "user not created.")              
        else:   
            user = UserForm()  
        user.operation = operations(request.user.id) 
        return render(request,"createuser.html",{'form':user}) 
    else:
        form = AuthenticationForm()
        return redirect('login')
    
def user_view(request):
    if request.user.is_authenticated:
            user_data = User.objects.all()
            rstr=''
            for i in user_data:
                role=user_roles.objects.filter(user_id_id=i.id)
                for j in role:
                    rstr = rstr+str(j.roles_id.role_name)+','
                print(rstr)
                i.roles=rstr
            user_data.operation = operations(request.user.id) 
            return render(request, 'userview.html', {'data': user_data})
    else:
        form = AuthenticationForm()
        return redirect('login')


def user_role(request):  
    if request.user.is_authenticated:    
        if request.method == "POST":  
            user = UserRoleForm(request.POST)  
            user_id   = request.POST['user']
            role_id = request.POST.getlist('roles') 
            users= User.objects.get(id=user_id)
            try:
               for rid in role_id:
                  roles = Roles.objects.get(id=rid)
                  user_roles.objects.create(user_id=users,roles_id=roles)
               messages.info(request, f"Roles assigned for users")
            except:  
               messages.error(request, "roles are not assigned for user.")
        else:   
            roles = UserRoleForm()
        roles.operation = operations(request.user.id)       
        return render(request,"createroles.html",{'form':roles})  
    else:
        form = AuthenticationForm()
        return redirect('login')
