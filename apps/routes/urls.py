from django.urls import path
from . import views

app_name = "routes"

urlpatterns = [
    path("",views.route_list,name="route_list"),
    path("create/", views.route_create, name="route_create"),
    path("<uuid:route_id>/",views.route_detail,name="route_detail"),

]
