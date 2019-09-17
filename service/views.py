import requests
import pytz
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Service, Location


class WeatherAPIView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            location = Location.objects.get(default=True)
            service = Service.objects.get(default=True)
            api_key = service.apikeystore_set.get(current_key=True)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)})
        payload = {'appid': api_key.key, 'units': 'metric',
                   'lat': location.lat, 'lon': location.lon}
        r = requests.get(service.url, params=payload)

        build_json = getattr(WeatherAPIView, service.available_service, None)
        if build_json is None:
            return Response({'error': 'Service not supported'})
        result = build_json(r.json())

        return Response(result)

    @staticmethod
    def openweathermap(data):
        result = {
            'location': {
                'lat': data['coord']['lat'],
                'lon': data['coord']['lon']
            },
            'title': data['name'],
            'timestamp': datetime.fromtimestamp(data['dt'],
                                                pytz.timezone('Europe/Moscow')),
            'temperature': {
                'C': data['main']['temp'],
            },
            'pressure': {
                'atm': data['main']['pressure']
            },
            'humidity': {
                'percent': data['main']['humidity']
            }
        }
        return result