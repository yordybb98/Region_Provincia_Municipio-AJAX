from django.db import models


class Region(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'


class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.provincia)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
