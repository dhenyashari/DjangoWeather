# from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=fd3347fcd07981743cf53ade32a327cd'
  city = 'Bali, ID'
  r = requests.get(url.format(city)).json()

  city_weather = {
    'city' : city,
    'temperature': r['main']['temp'],
    'description': r['weather'][0]['description'],
    'icon': r['weather'][0]['icon'],
  }
  print(city_weather)
  context = {'city_weather': city_weather}
  return render(request, 'weather/weather.html', context)
  # print (r)
  # return HttpResponse(r)