from datetime import datetime
from accounts.models import Person,User
from rest_framework.permissions import BasePermission
from accounts.models import Granted
from django.db.models import F

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_superuser and request.user.is_staff) or request.user.user_type == 'P';

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_superuser and request.user.is_staff) or request.user.user_type == 'D';

class IsAuthDoctor(BasePermission):
    def has_permission(self, request, view):
        asking_user:User=request.user
        pk=request.GET.get('resource_owner',None)
        try:
            if not pk:
                pk=request.data['resource_owner']
            pk=int(pk)
        except:
            print('Error: resource_owner must be present in data or in request parameter')
            print('Resource_owner integer parameter, it donote primary key of owner')
            print('Error raised by IsAuthDoctor permission')
            return False
        print('bhdsb')
        try:
            granting_user:User=User.objects.get(pk=pk)
        except:
            print('Error: Invalid user ID in resource owner')
            print('Resource_owner integer parameter, it donote primary key of owner')
            print('Error raised by IsAuthDoctor permission')
            return False;
        print(granting_user,asking_user,granting_user.user_type)
        if asking_user.user_type=='D' and granting_user.user_type=='P':
            grants=Granted.objects.filter(asking_user=asking_user,granting_user=granting_user)
            print('abc',grants)
            grants=grants.filter(duration__gte=datetime.today()-F('granted_at'))
            print('pqr',grants)
            return (request.user.is_superuser and request.user.is_staff) or grants.exists();
        print('bhdsb1')
        return False;
class IsActive(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active;
