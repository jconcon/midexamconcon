from django.db import models
from django.utils import timezone
# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=250)
    content = models.CharField(max_length=250)



    def __str__(self):
	       return str(self.name)

class Candidate(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    birthdate = models.DateTimeField(default=timezone.now)
    platform = models.TextField()
    def __str__(self):
        return str(self.position)

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    vote = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.candidate)
