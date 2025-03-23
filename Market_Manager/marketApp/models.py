from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Product(models.Model):
    TYPE_CHOICES = [
        ("F", "Food"),
        ("D", "Drinks"),
        ("B", "Bakery"),
        ("C", "Cosmetics"),
        ("H", "Hygiene"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    is_homemade = models.BooleanField()
    code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.type}"


class Contact(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.IntegerField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.street} {self.street_number} {self.phone_number}, {self.email}"


class Market(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.OneToOneField(Contact, on_delete=models.CASCADE)
    num_markets = models.IntegerField()
    opening_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    embg = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ProductMarket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.market} ({self.quantity})"
