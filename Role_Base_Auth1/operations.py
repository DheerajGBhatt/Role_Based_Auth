from Roles.models import *
from Users.models import *
from django.contrib.auth.models import User
def operations(user_id):
    result=list()
    users=user_roles.objects.filter(user_id_id=user_id)
    for user in users:
       #result.append(user.roles_id.role_name)
       r_action = role_action.objects.filter(role_id_id=user.roles_id.id)
       for j in r_action:
                result.append(j.action_id.action_name)
       r_resource = role_resource.objects.filter(role_id_id=user.roles_id.id)
       for k in r_resource:
               result.append(k.resource_id.resource_name)
    return(list(set(result)))
          
