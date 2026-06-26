from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname