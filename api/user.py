from django.contrib.auth.models import User
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource


class UserResource(ModelResource):
   class Meta:
      queryset = User.objects.all()
      resource_name = 'user'
      fields = [
         'username',
         'first_name',
         'last_name',
         'last_login',
      ]
      authentication = SessionAuthentication()
      authorization = DjangoAuthorization()
