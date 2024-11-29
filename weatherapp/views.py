from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.

def get_weather_data(request):
    api_key = "9719a6a0294835eee9b0d447db510b56"  # Replace this with your actual OpenWeatherMap or weather.com API key
    city = request.GET.get('city', 'London')  # You can modify the city as per user input

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'humidity': data['main']['humidity'],
                'timezone': data['timezone'] // 3600,  # Convert from seconds to hours
        }
    else:
        weather_info = {'error': 'City not found'}

    return JsonResponse(weather_info)

def show_weather(request):
    return render(request, 'weatherapp/weather.html')

