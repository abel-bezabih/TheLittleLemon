from django.db import models

# MenuItem model
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {self.price:.2f}'  # Ensure price always has two decimal places

# Booking model
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        # Ensure booking_date is a datetime object and format it as a string
        return f'{self.name} - {self.no_of_guests} guests on {self.booking_date.strftime("%Y-%m-%d")}'
