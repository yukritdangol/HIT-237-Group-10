from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    regiom = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Housing (models.Model):
    title = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title