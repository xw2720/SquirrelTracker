"""squirrel_tracker_site URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # , include
# from squirrel_tracker.views import MapView
from squirrel_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # ----
    # path('map/', MapView.as_view(), name='map'),
    path('map/', views.map_view, name='map'),
    path('sightings/', views.sightings, name='sighting'),
    path('sightings/add/', views.sightings_add, name='add'),
    # ----
    path('sightings/stats/', views.sightings_stats, name='stats'),
    path('sightings/<squirrel_id>/', views.sightings_update, name='update'),
]
