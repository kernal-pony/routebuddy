from django import forms

from .models import *


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route

        fields = [
            "title",
            "description",
            "origin",
            "destination",
            "transport_type",
        ]