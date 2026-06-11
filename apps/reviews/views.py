from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from apps.routes.models import Route

from .forms import ReviewForm
from .models import Review
@login_required
def review_create(request, route_id):

    route = get_object_or_404(
        Route,
        id=route_id
    )

    if Review.objects.filter(
        route=route,
        user=request.user
    ).exists():

        messages.error(
            request,
            "You have already reviewed this route."
        )

        return redirect(
            "routes:route_detail",
            route_id=route.id
        )

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(
                commit=False
            )

            review.route = route

            review.user = request.user

            review.save()

            messages.success(
                request,
                "Review added successfully."
            )

            return redirect(
                "routes:route_detail",
                route_id=route.id
            )

    else:

        form = ReviewForm()

    context = {
        "form": form,
        "route": route,
    }

    return render(request, "reviews/review_form.html", context)