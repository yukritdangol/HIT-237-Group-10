from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('USER', 'Community User'),
    ('MANAGER', 'Housing Manager'),
    ('ADMIN', 'Admin'),
)

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='USER'
    )

    community_name = models.CharField(
        max_length=100
    )

    contact_number = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.user.username