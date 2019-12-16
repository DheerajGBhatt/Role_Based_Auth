from django import forms
from Roles.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Users.models import * 

class UserRoleForm(forms.Form):
        user= forms.CharField(label='Roles', widget=forms.Select(choices=[(option.id, option.username) for option in
             User.objects.all()]) ) 
        roles=forms.MultipleChoiceField(choices=[(option.id, option.role_name) for option in Roles.objects.all()], widget=forms.CheckboxSelectMultiple,)
                

