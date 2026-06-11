import uuid

from django.conf import settings
from django.db import models

class TransportType(models.Model):
    """
    Lookup table for transport categories.
    Examples:
    - Bus
    - Metro
    - Auto
    - Ferry
    """

    name = models.CharField(
        max_length=50,
        unique=True
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# -----------------------------------
class Route(models.Model):
    """
    Community-created transportation route.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    origin = models.CharField(max_length=200)

    destination = models.CharField(max_length=200)

    transport_type = models.ForeignKey(TransportType, on_delete=models.PROTECT, related_name="routes")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="routes")

    is_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# -----------------------------------

from django.db import models


class Stop(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "city"],
                name="unique_stop_name_city"
            )
        ]

    def __str__(self):
        return f"{self.name}, {self.city}"


# -------------------------------------------------

from django.db import models


class RouteStop(models.Model):
    route = models.ForeignKey(
        "Route",
        on_delete=models.CASCADE,
        related_name="route_stops"
    )

    stop = models.ForeignKey("Stop", on_delete=models.PROTECT, related_name="route_stops")

    stop_order = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["stop_order"]

        constraints = [
            models.UniqueConstraint(
                fields=["route", "stop_order"],
                name="unique_route_stop_order"
            ),
            models.UniqueConstraint(
                fields=["route", "stop"],
                name="unique_route_stop"
            ),
            models.CheckConstraint(
                condition=models.Q(stop_order__gt=0),
                name="stop_order_positive"
            )
        ]

    def __str__(self):
        return (
            f"{self.route.title} - "
            f"{self.stop_order} - "
            f"{self.stop.name}"
        )

