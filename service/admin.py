from django.contrib import admin
from .models import Service, Location, APIKeyStore, Parameter, Header


@admin.register(APIKeyStore)
class APIKeyStoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'current_key', 'is_header', 'attr_name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'default', 'available_service', 'url']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'lon', 'lat', 'default']


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ['title', 'value']


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'value']
