from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to='images/')
    cv = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.school
        
class certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

