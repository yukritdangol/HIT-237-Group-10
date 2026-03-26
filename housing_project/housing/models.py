from django.db import models

class Housing(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title