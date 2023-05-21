from django.db import models

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    pc = models.CharField(max_length=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name + str(self.age) + self.gender + self.pc