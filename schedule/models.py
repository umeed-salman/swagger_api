from django.db import models

class Schedule(models.Model):
    day_of_week = models.CharField(max_length=10)  # e.g., 'monday', 'tuesday', etc.
    start_time = models.TimeField()
    stop_time = models.TimeField()
    ids = models.JSONField()  # Storing IDs as a list

    class Meta:
        unique_together = ('day_of_week', 'start_time', 'stop_time')

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.stop_time}"
