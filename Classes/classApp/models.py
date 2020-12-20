from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=50, default='', blank=True, null=False)
    course_number = models.IntegerField(max_length=20, blank=True, null=False)
    instructor_name = models.CharField(max_length=50, blank=True, null=False)
    duration = models.FloatField(max_length=50, blank=True, null=False)

    objects = models.Manager()