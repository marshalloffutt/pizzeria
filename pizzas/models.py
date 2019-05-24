from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A class to resemble a pizza one might order"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representing name of pizza"""
        return self.name

class Topping(models.Model):
    """A class to resemble a topping one might want on their pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.TextField()

    def __str__(self):
        """Return a string representation of the topping."""
        return self.topping