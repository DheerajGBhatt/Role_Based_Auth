from django.shortcuts import render
from Roles.forms.rolesform import *
from Roles.forms.roles_resourceform import *
from Roles.forms.roles_actionform import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Roles.models import *
from django.contrib import messages
from operations import *

# Create your views here.
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            roles = RolesForm(request.POST)
            if roles.is_valid():
              try:
                roles.save()
                messages.info(request, "role created")
                return redirect('home')
              except:
               messages.error(request, "user not created.")
        else:
            roles = RolesForm()
        roles.operation = operations(request.user.id)
        return render(request,"createroles.html",{'form':roles})
    else:
        form = AuthenticationForm()
        return redirect('login')

def roles_action(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            roles = RolesActionForm(request.POST)
            role_id   = request.POST['role']
            action_id = request.POST.getlist('actions')
            role = Roles.objects.get(id=role_id)

            try:
               for aid in action_id:
                  action = Action.objects.get(id=aid)
                  role_action.objects.create(role_id=role,action_id=action)
               messages.info(request, f"actions assigned for roles")
            except:
               messages.error(request, "actions not assigned.")
            return redirect('home')
        else:
            roles = RolesActionForm()
            roles.action1=Action.objects.all()
            roles.roles1=Roles.objects.all()
            roles.operation = operations(request.user.id)
            return render(request,"assignaction.html",{'form':roles})
        roles.operation = operations(request.user.id)
        return render(request,"createroles.html",{'form':roles})
    else:
            form = AuthenticationForm()
            return redirect('login')

def roles_resource(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            roles = RolesResourceForm(request.POST)
            role_id   = request.POST['role']
            resource_id = request.POST.getlist('resource')
            role = Roles.objects.get(id=role_id)
            try:
               for aid in resource_id:
                  resource = Resources.objects.get(id=aid)
                  role_resource.objects.create(role_id=role,resource_id=resource)
               messages.info(request, f"Resources are assigned for roles")
            except:
               messages.error(request, "resources not assigned.")
            return redirect('home')

        else:
            roles = RolesResourceForm()
            roles.resource1=Resources.objects.all()
            roles.roles1=Roles.objects.all()
            roles.operation = operations(request.user.id)
            return render(request,"assignresource.html",{'form':roles})

    else:
            return redirect('login')

def roles_view(request):
    if request.user.is_authenticated:
        roles_data = Roles.objects.all()

        for i in roles_data:
            astr=''
            rstr=''
            r_action = role_action.objects.filter(role_id_id=i.id)
            for j in r_action:
                if str(j.action_id.action_name) in astr:
                    pass
                else:
                    astr=astr+str(j.action_id.action_name)+','
            r_resource = role_resource.objects.filter(role_id_id=i.id)
            for k in r_resource:
                if str(k.resource_id.resource_name) in rstr:
                    pass
                else:
                    rstr=rstr+str(k.resource_id.resource_name)+','
            i.actions=astr
            i.resources=rstr
        roles_data.operation = operations(request.user.id)
        return render(request, 'rolesview.html', {'data': roles_data})
    else:

            return redirect('login')