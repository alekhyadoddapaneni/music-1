from django.db import models

class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    salary = models.FloatField()

    def __str__(self):
        return self.name
