from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A class to resemble a pizza one might order"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representing name of pizza"""
        return self.name
