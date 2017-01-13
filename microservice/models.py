from django.db import models

class Fellows(models.Model):
    name = models.CharField(max_length=100)
    cohort = models.IntegerField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name
