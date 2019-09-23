import requests
import pytz
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Location, APIKeyStore


class WeatherAPIView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            location = Location.objects.get(default=True)
            api_key_obj = APIKeyStore.objects.select_related('service').get(current_key=True, service__default=True)
            service = api_key_obj.service
            payload = {name: value for name, value in service.parameter_set.values('title', 'value')}
            headers = {name: value for name, value in service.header_set.values('title', 'value')}
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)})

        api_key_attr = {api_key_obj.attr_name: api_key_obj.key}
        if api_key_obj.is_header:
            headers.update(api_key_attr)
        else:
            payload.update(api_key_attr)

        payload.update({'lat': location.lat, 'lon': location.lon})

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
