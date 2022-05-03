from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length= 255)
    roll = models.IntegerField(default= 0)
    phone = models.IntegerField()
    address = models.CharField(max_length= 255)
    def __str__(self):
        return self.name + '-' + self.address
      
   
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject  = models.CharField(max_length=50)
    salary = models.IntegerField()
    is_principal = models.BooleanField()

    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
class Books(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    name = models.CharField(max_length= 255)
    no_pgs = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
class AuthorPenName(models.Model):
    pen_name = models.CharField(max_length=255)
    author = models.OneToOneField(Author, on_delete= models.CASCADE)

class TutionStudent(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=244)
    booked = models.ManyToManyField(Books)
