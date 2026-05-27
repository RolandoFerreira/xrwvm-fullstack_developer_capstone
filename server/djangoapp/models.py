from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'WAGON'
    COUPE = 'Coupe'
    TRUCK = 'Truck'
    
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (TRUCK, 'Truck'),
    ]
    
    name = models.CharField(null=False, max_length=30)
    type = models.CharField(
        null=False,
        max_length=10,
        choices=CAR_TYPES,
        default=SEDAN
    )
    year = models.IntegerField(
        null=False,
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Type: " + self.type + "," + \
               "Year: " + str(self.year)