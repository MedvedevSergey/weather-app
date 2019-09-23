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
    is_header = models.BooleanField(default=False)
    attr_name = models.CharField(max_length=15, default='appid')

    def __str__(self):
        return self.name


class Abstract(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Parameter(Abstract):
    pass


class Header(Abstract):
    pass
