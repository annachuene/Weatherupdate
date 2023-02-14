from django.urls import path
from .views import get_weather, add_to_database,get_all_weather_data

urlpatterns = [
    path('', get_weather, name='get_weather'),
    path('get_weather', get_weather, name='get_weather'),
    path('add_to_database', add_to_database, name='add_to_database'),
    path('get_all_weather_data', get_all_weather_data, name='get_all_weather_data'),
]