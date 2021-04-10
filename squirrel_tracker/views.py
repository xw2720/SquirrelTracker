from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from squirrel_tracker.models import Squirrel


def index(request):
    return redirect('map/')


# Create your views here.

class MapView(TemplateView):
    """
    Merge from Wendy's original seperated project
    ref: https://docs.djangoproject.com/zh-hans/3.1/topics/class-based-views/
    """
    template_name = "map/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO add query of squirrel data here
        sightings = Squirrel.objects.all()
        context["sightings"] = sightings
        return context
