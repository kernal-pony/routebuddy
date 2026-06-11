from django.conf import settings
from django.db import models
from django.db.models import Q

from apps.routes.models import Route


class Review(models.Model):

    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="reviews")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,blank=True, related_name="reviews")

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_at"]

        constraints = [

            models.UniqueConstraint(
                fields=["route", "user"],
                name="unique_review_per_user_per_route"
            ),

            models.CheckConstraint(
                condition=Q(rating__gte=1) & Q(rating__lte=5),
                name="rating_between_1_and_5"
            ),
        ]

    def __str__(self):
        return f"{self.route} - {self.rating}"