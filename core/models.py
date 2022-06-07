from django.db import models
from numpy import percentile

# Create your models here.

#Portfolio Models
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class TechnicalSkill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProffessionalSkill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name