from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name} "


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_of_publishing = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    cover_image = models.ImageField(upload_to='covers/',null=True, blank=True)
    available = models.BooleanField()

    def __str__(self):
        return f"{self.title} {self.author} {self.genre}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField()
    comment = models.CharField(max_length=400)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade} "



class BookTranslator(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} -> {self.translator}"