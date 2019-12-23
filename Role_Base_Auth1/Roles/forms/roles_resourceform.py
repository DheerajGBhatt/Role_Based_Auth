from django import forms
from Roles.models import *
from django.contrib.auth.models import User
from Users.models import *

class RolesResourceForm(forms.Form):
       roles =Roles.objects.all()
       roles.count()
       role= forms.CharField(label='Roles', widget=forms.Select(choices=[(option.id, option.role_name) for option in roles ]) )
       resource=forms.MultipleChoiceField(choices=[(option.id, option.resource_name) for option in Resources.objects.all()], widget=forms.CheckboxSelectMultiple,)
