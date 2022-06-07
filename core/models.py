from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

#import RichTextField
from ckeditor.fields import RichTextField


# Create your models here.

#Portfolio Models
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    proffession = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100,  blank=True, null=True)
    linkedin = models.CharField(max_length=100,  blank=True, null=True)
    github = models.CharField(max_length=100,  blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 100},
    )
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class ProffessionalSkill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about/images/')
    cv = models.FileField(upload_to='about/cv/', blank=True)

    class Meta:
        verbose_name_plural = 'About Me'


    def __str__(self):
        return f"main {self.pk}"



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

class MyTechStach(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fa_object = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    achievement = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    #richtextfield
    description = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name