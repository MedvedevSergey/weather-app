from django.db import models


class Service(models.Model):
    SERVICES = (
        ('openweathermap', 'openweathermap'),
    )

    title = models.CharField(max_length=255, verbose_name='Название сервиса')
    url = models.URLField()
    default = models.BooleanField(default=False,
                                  verbose_name='Сервис по умолчанию')
    available_service = models.CharField(max_length=30, default=SERVICES[0][0],
                                         choices=SERVICES)

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название локации')
    lon = models.FloatField()
    lat = models.FloatField()
    default = models.BooleanField(default=False,
                                  verbose_name='Мстоположения по умолчанию')

    def __str__(self):
        return self.title


class APIKeyStore(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    current_key = models.BooleanField(default=False)

    def __str__(self):
        return self.name
