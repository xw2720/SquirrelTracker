from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    pass
    # return render(request, 'sightings/index.html', context)


# Create your views here.

class MapView(TemplateView):
    template_name = "map/map.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
