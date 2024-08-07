from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length = 255)
    No_of_guests = models.IntegerField(max_length = 6)
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    ID = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

