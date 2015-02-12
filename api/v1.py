from tastypie.api import Api

from .user import UserResource

api = Api(api_name='v1')
api.register(UserResource())

