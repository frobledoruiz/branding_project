from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class Contractor(models.Model):
    """
    Modelo para crear base de datos de contratistas
    Cada contratista puede tener múltiples usuarios
    Cada usuario puede tener asignado varios grupos
    Los grupos están asociados con los permisos, que son funcionalidad de Django

    """

    WORK_SCOPE = (('I', 'Instalación Imagen'), ('T', 'Instalación Tanques'),
                  ('C', 'Consuloría'))

    COUNTRY_ZONE = (('N', 'Norte'), ('C', 'Centro'), ('S', 'Sur'))

    contractor_name = models.CharField(default=None, max_length=100)
    contractor_scope = models.CharField(
        default="I", max_length=1, choices=WORK_SCOPE)
    contractor_zone = models.CharField(
        default="N", max_length=1, choices=COUNTRY_ZONE)
    contractor_date_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.contractor_name