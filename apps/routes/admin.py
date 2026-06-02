from django.contrib import admin
from .models import *

admin.site.register(TransportType)
admin.site.register(Route)
admin.site.register(Stop)
admin.site.register(RouteStop)