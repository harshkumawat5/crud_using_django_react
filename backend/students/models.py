from django.db import models

# Create your models here.


class Student(models.Model):
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True,blank=True)

    

    def __str__(self):
        return self.name