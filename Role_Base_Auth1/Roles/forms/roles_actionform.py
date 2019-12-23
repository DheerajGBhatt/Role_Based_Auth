from django import forms
from Roles.models import *
from django.contrib.auth.models import User
from Users.models import *
from django.forms import ModelMultipleChoiceField

class RolesActionForm(forms.Form):
        roles=Roles.objects.all()
        roles.count()
        role= forms.CharField(label='Roles', widget=forms.Select(choices=[(option.id, option.role_name) for option in roles]) )
        actions=forms.MultipleChoiceField(choices=[(option.id, option.action_name) for option in Action.objects.all()], widget=forms.CheckboxSelectMultiple,)

