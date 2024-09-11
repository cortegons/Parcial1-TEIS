from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class flight(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    precio = models.PositiveIntegerField(validators=[MinValueValidator(1)])