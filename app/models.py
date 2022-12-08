from django.db import models


CHOOSE_STATUS=(('LATE','LATE'),('ON_TIME','ON_TIME'),('CANCELLED','CANCELLED'),('ARRIVED','ARRIVED'))

# Create your models here.
class TrainDetails(models.Model):
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=30,choices=CHOOSE_STATUS)

    def __str__(self):
        return self.name