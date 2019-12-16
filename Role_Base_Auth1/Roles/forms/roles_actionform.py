from django import forms
from Roles.models import *
from django.contrib.auth.models import User
from Users.models import *
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget 
class RolesActionForm(forms.Form):
        role= forms.CharField(label='Roles', widget=forms.Select(choices=[(option.id, option.role_name) for option in
             Roles.objects.all()]) ) 
        actions=forms.MultipleChoiceField(choices=[(option.id, option.action_name) for option in Action.objects.all()], widget=forms.CheckboxSelectMultiple,)
                
