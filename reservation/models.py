from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"


class Book(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return self.name

# 7a38e83ac0fdd2f47cc58bf9c08c1cd9299c2bf2
