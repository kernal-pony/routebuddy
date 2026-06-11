from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [

    path("routes/<uuid:route_id>/review/", views.review_create, name="create",),


]