from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    tenth_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    contact_number = models.CharField(max_length=15)
    passing_year = models.IntegerField()
    current_school = models.CharField(max_length=200)
    interested_branch = models.CharField(max_length=100)

    def __str__(self):
        return self.name
