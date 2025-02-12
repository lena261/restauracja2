
from django.db import models

# Create your models here.
# propozycje modeli: GuestName, date, hour,  table

class GuestName(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class DateTime(models.Model):
    dateTime = models.DateTimeField()



class Place(models.TextChoices):
    OUTSIDE = 'outside', 'Outside'
    INSIDE = 'inside', 'Inside'

class MyModel(models.Model):
    name = models.CharField(max_length=255)  # np. nazwa obiektu
    place = models.CharField(
        max_length=10,
        choices=Place.choices,
        default=Place.OUTSIDE
    )

class Table(models.Model):
    quantity = models.PositiveIntegerField()
    place = models.CharField(
        max_length=10,
        choices=Place.choices,
        default=Place.OUTSIDE
    )
    TableNumber = models.PositiveIntegerField(unique=True)  # Numer stolika jako liczba całkowita

    def __str__(self):
        return f"Stolik nr {self.TableNumber} ({self.place} - {self.quantity} miejsc)"


class Reservation(models.Model):
    lastname = models.ForeignKey(GuestName, on_delete=models.CASCADE)
    TableNumber = models.ForeignKey(Table,on_delete=models.CASCADE )
    #numer stolika
    guestNumber = models.PositiveIntegerField()
    dateTime = models.DateTimeField()
    
    def __str__(self):
        return f"Rezerwacja dla {self.lastname} na stoliku nr {self.TableNumber.TableNumber}"