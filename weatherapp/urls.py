from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_weather, name='show_weather'),
    path('api/weather/', views.get_weather_data, name='get_weather_data'),
    
    # path('weather/', views.weather, name='weather'),
    ]