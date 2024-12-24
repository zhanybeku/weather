from django.shortcuts import render
from decouple import config
from datetime import datetime as dt
import requests

# Create your views here.
def index(request):
  return render(request, "app/index.html")

def request_to_weather_api(city):
  URL = f"http://api.weatherapi.com/v1/current.json?key={config("WAPI_KEY")}&q={city}"
  res = requests.get(URL)
  res.raise_for_status()
  res_json = res.json()
  return {
    "city": res_json["location"]["name"],
    "description": res_json["current"]["condition"]["text"],
    "icon": f'http: {res_json["current"]["condition"]["icon"]}',
    "temperature": res_json["current"]["temp_c"],
    "updated_date": dt.fromtimestamp(res_json["current"]["last_updated_epoch"]).strftime('%Y-%m-%d'),
    "api_response": res.text
  }