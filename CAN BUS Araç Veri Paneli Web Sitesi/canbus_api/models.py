from django.db import models

# Araç verilerini veritabanında temsil edecek olan model.
class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=20, primary_key=True, unique=True)
    timestamp = models.DateTimeField()
    status = models.JSONField()
    diagnostics = models.JSONField()
    location = models.JSONField()

    def __str__(self):
        return self.vehicle_id