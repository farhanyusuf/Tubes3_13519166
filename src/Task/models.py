from django.db import models
from django.db.models.fields import TextField, DateField

class Task(models.Model):
    tanggal = models.DateField(blank=False)
    kodematakuliah = models.TextField(blank=False)
    jenistugas = models.TextField(blank=False)
    topiktugas = models.TextField(blank=False)

class KeyWord(models.Model):
    word = models.TextField(blank=False)
    tipe = models.TextField(blank=False, default=None)
    
# Create your models here.
