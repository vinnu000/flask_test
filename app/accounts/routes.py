from . import accounts_api

from .views import Home

accounts_api.add_resource(Home, '/')
