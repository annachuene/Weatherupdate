from django.shortcuts import render, HttpResponse
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from .models import WeatherData

import json

# Load the environment variables from the .env file
load_dotenv()

def get_all_weather_data(request):
    weather_data = WeatherData.objects.all()
    data = []
    for item in weather_data:
        data.append({
            "city_name": item.city_name,
            "temperature": item.temperature,
            "humidity": item.humidity,
            "description": item.description,
            "icon": item.icon
        })
    print(data)
    return JsonResponse({'weather_data': data})

def get_weather(request):
    city = request.GET.get("city", None)
    mapbox_API_KEY = os.getenv('MAPBOX_API_KEY')
    openweathermap_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
    if city:
        # get longitude and latitude using Mapbox API
        mapbox_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{city}.json?access_token={mapbox_API_KEY}"
        response = requests.get(mapbox_url).json()
        try:
            longitude = response["features"][0]["center"][0]
            latitude = response["features"][0]["center"][1]
        except IndexError:
            return JsonResponse({'error': 'City not found'})

        # get weather using OpenWeather API
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={openweathermap_API_KEY}"
        weather_response = requests.get(weather_url).json()

        # Check if the request was successful
        if weather_response.get('cod') == 200:
            weather_data = {
                'city_name': weather_response['name'],
                'temperature': weather_response['main']['temp'],
                'description': weather_response['weather'][0]['description'],
                'icon': weather_response['weather'][0]['icon'],
                'humidity': weather_response['main']['humidity']
            }
            print(weather_response)
            return JsonResponse({'weather_data': weather_data})
        else:
            return JsonResponse({'error': 'An error occurred while retrieving the weather data'})
    else:
        return render(request, 'weather_app/index.html')


def add_to_database(request):
    city_name = request.POST.get('city_name')
    temperature = request.POST.get('temperature')
    description = request.POST.get('description')
    icon = request.POST.get('icon')
    humidity = request.POST.get('humidity')

    WeatherData.objects.create(
        city_name=city_name,
        temperature=temperature,
        description=description,
        icon=icon,
        humidity=humidity
    )
    return JsonResponse({'success': 'Data added to the database'})