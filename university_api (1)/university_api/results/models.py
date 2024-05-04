# from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     reg_no = models.CharField(max_length=20, unique=True)
#     math_marks = models.DecimalField(max_digits=5, decimal_places=2)
#     dob = models.DateField()
#     stats_marks = models.DecimalField(max_digits=5, decimal_places=2)
#     compsci_marks = models.DecimalField(max_digits=5, decimal_places=2)
#     english_marks = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return self.name
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
