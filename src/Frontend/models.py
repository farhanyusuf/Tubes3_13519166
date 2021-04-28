from django.db import models

# Create your models here.
class Message(models.Model) :
    name = models.TextField()
    text = models.TextField()

    def print(self):
        print(self.name)
        print(self.text)