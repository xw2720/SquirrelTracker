from django.urls import path
from squirrel_tracker.views import MapView

app_name = 'map'
urlpatterns = [
    path('', MapView.as_view(), name='map'),
]
