from django.shortcuts import (get_object_or_404, render, redirect)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *


def route_detail(request,route_id):
    route = get_object_or_404(Route,id=route_id,is_active=True)

    route_stops = (route.route_stops.select_related("stop").all())

    context = {
        "route": route,
        "route_stops": route_stops,
    }
    return render(request,"routes/route_detail.html",context)


def route_list(request):
    routes = Route.objects.filter(is_active=True).select_related("transport_type","created_by")

    context = {
        "routes": routes
    }

    return render(request, "routes/route_list.html", context)

@login_required
def route_create(request):

    if request.method == "POST":

        form = RouteForm(request.POST)

        if form.is_valid():

            route = form.save(commit=False)

            route.created_by = request.user

            route.is_verified = False

            route.save()
            messages.success(
                request,
                "Route created successfully and is pending verification."
            )

            return redirect("routes:route_detail", route_id=route.id)

    else:

        form = RouteForm()

    context = {
        "form": form
    }

    return render(request, "routes/route_create.html", context)