from django.db import models
from Roles.models import *
from django.contrib.auth.models import User

class user_roles(models.Model):
   user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
   roles_id = models.ForeignKey(Roles, on_delete=models.CASCADE) 