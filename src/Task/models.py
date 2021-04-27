from django.db import models
from django.db.models.fields import TextField

class Task(models.Model):
    tanggal = models.TextField(blank=False)
    kodematakuliah = models.TextField(blank=False)
    jenistugas = models.TextField(blank=False)
    topiktugas = models.TextField(blank=False)


# Create your models here.
