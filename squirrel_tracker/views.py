from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from squirrel_tracker.models import Squirrel


# Create your views here.

def index(request):
    # redirect our homepage to map view
    return redirect('map/')


# [:100] 限制marker实际显示在map上的个数
def map_view(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
        'sightings': sightings,
    }
    return render(request, 'map/map.html', context)


def sightings(request):
    # TODO template file by wendy
    context = {}
    return render(request, 'sightings/sightings.html', context)


def sightings_add(request):
    # TODO template file by wendy
    context = {}
    return render(request, 'sightings/add.html', context)


def sightings_stats(request):
    # TODO
    context = {}
    return render(request, 'sightings/stats.html', context)


def sightings_update(request, squirrel_id):
    # TODO
    print("(debug) squirrel_id: ", squirrel_id)
    context = {}
    return render(request, 'sightings/update.html', context)

# class MapView(TemplateView):
#     """
#     Merge from Wendy's original seperated project
#     ref: https://docs.djangoproject.com/zh-hans/3.1/topics/class-based-views/
#     """
#     template_name = "map/map.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # TODO add query of squirrel data here
#         sightings = Squirrel.objects.all()
#         context["sightings"] = sightings
#         return context
