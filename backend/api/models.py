from django.db import models
from django.utils import timezone

# Create your models here.

class AttendanceLog(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    computingID = models.TextField()
    dateLogged = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.computingID