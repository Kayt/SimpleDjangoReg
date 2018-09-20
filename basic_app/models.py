from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
)

# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User)

    gender = models.CharField(max_length=128, choices=GENDER, default='FEMALE')
    age = models.IntegerField(validators=[MinValueValidator(16),
                                       MaxValueValidator(100)])

    def __str__(self):
        return self.user.username
