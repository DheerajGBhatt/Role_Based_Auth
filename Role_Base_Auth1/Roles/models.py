from django.db import models

# Create your models here.
class Roles(models.Model):
      role_name    = models.CharField(blank=True,max_length=200)
      description  = models.CharField(blank=True,max_length=1000)

class Action(models.Model):
   action_name   = models.CharField(blank=True,max_length=200)
   description  = models.CharField(blank=True,max_length=1000)

class Resources(models.Model):
   resource_name   = models.CharField(blank=True,max_length=200)
   description  = models.CharField(blank=True,max_length=1000)

class role_action(models.Model):
       role_id   =  models.ForeignKey(Roles, on_delete=models.CASCADE)
       action_id   =  models.ForeignKey(Action, on_delete=models.CASCADE)
 
class role_resource(models.Model):
       resource_id   =  models.ForeignKey(Resources, on_delete=models.CASCADE)
       role_id   =  models.ForeignKey(Roles, on_delete=models.CASCADE) 
