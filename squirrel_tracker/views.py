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
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/sightings.html', context)


def sightings_add(request):
    form = SquirrelForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            added_squirrel = form.save(commit=False)
            added_squirrel.save()
            squirrel_id = added_squirrel.Unique_squirrel_id
            return redirect(f'/sightings/{squirrel_id}')

    context = {
         'form': form,
    }
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
    squirrel = get_object_or_404(Squirrel, Unique_squirrel_id=squirrel_id)
    form = SquirrelForm(request.POST or None, instance=squirrel)

    if request.method == 'POST':
        if form.is_valid():
            updated_squirrel = form.save(commit=False)
            updated_squirrel.save()
            squirrel_id = updated_squirrel.Unique_squirrel_id
            return redirect(f'/sightings/#{squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }
    return render(request, 'sightings/update.html', context)
