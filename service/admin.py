from django.contrib import admin
from .models import Service, Location, APIKeyStore


@admin.register(APIKeyStore)
class APIKeyStoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'current_key']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'default', 'available_service', 'url']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'lon', 'lat', 'default']
