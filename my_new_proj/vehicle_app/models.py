from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Two', 'Two Wheeler'),
        ('Three', 'Three Wheeler'),
        ('Four', 'Four Wheeler'),
    ]
    
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=50)
    vehicle_description = models.TextField()

    def __str__(self):
        return f"{self.vehicle_number} - {self.vehicle_model}"

