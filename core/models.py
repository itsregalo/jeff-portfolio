from django.db import models
from pendulum import duration
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

#import RichTextField


# Create your models here.

#Portfolio Models
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    proffession = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
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

class AboutMe(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about/images/')
    cv = models.FileField(upload_to='about/cv/', blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ProcessedImageField(
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 100},
        upload_to='projects/images/'
    )
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
