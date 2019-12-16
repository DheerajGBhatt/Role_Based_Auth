from django import forms
from Roles.models import *
from django.contrib.auth.models import User
from Users.models import *
class RolesForm(forms.ModelForm):  
        
        class Meta:
                model = Roles
                fields = '__all__'
