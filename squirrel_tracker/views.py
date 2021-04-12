from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from squirrel_tracker.models import Squirrel
from squirrel_tracker.forms import SquirrelForm


# Create your views here.

def index(request):
    return render(request, 'indexing/indexing.html', {})


# [:100] 限制marker实际显示在map上的个数
def map_view(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
        'sightings': sightings,
    }
    return render(request, 'map/map.html', context)


def sightings(request):
    # TODO template file by wendy
    ##
    squirrel = Squirrel.objects.all()
    context = {'Squirrel': squirrel}
    return render(request, 'sightings/sightings.html', context)


def sightings_add(request):
    # TODO template file by wendy
    context = {}
    return render(request, 'sightings/add.html', context)


def sightings_stats(request):
    total = Squirrel.objects.all().count()
    gray_fur = Squirrel.objects.filter(Primary_fur_color=Squirrel.GRAY).count()
    cinnamon_fur = Squirrel.objects.filter(Primary_fur_color=Squirrel.CINNAMON).count()
    juvenile_age = Squirrel.objects.filter(Age=Squirrel.JUVENILE).count()
    adult_age = Squirrel.objects.filter(Age=Squirrel.ADULT).count()
    ground_plane_location = Squirrel.objects.filter(
        Location=Squirrel.GROUND_PLANE).count()
    above_ground_plane_location = Squirrel.objects.filter(
        Location=Squirrel.ABOVE_GROUND).count()
    running = Squirrel.objects.filter(Running=True).count()
    chasing = Squirrel.objects.filter(Chasing=True).count()
    climbing = Squirrel.objects.filter(Climbing=True).count()
    eating = Squirrel.objects.filter(Eating=True).count()
    context = {  # 这里是排下顺序，顺便显示下给人看的名字，注释待会删除
        'stat_cols': [
            [
                'total', 'Total of squirrel sightings',
            ],
            [
                'gray_fur', 'Squirrel that has gray fur',
            ],
            [
                'cinnamon_fur', 'Squirrel that has cinnamon fur',
            ],
            [
                'juvenile_age', 'Squirrel at juvenile age',
            ],
            [
                'adult_age', 'Squirrel at adult age',
            ],
            [
                'ground_plane_location', 'Squirrel at ground plane location',
            ],
            [
                'above_ground_plane_location', 'Squirrel above ground plane location',
            ],
            [
                'running', 'Squirrel that is running',
            ],
            [
                'chasing', 'Squirrel that is chasing',
            ],
            [
                'climbing', 'Squirrel that is climbing',
            ],
            [
                'eating', 'Squirrel that is eating',
            ],
        ],
        'stats': {
            'total': total,
            'gray_fur': gray_fur,
            'cinnamon_fur': cinnamon_fur,
            'juvenile_age': juvenile_age,
            'adult_age': adult_age,
            'ground_plane_location': ground_plane_location,
            'above_ground_plane_location': above_ground_plane_location,
            'running': running,
            'chasing': chasing,
            'climbing': climbing,
            'eating': eating,
        }

    }
    return render(request, 'sightings/stats.html', context)


def sightings_update(request, squirrel_id):
    print("(debug) squirrel_id: ", squirrel_id)

    squirrel = Squirrel.objects.get(Unique_squirrel_id=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }
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
