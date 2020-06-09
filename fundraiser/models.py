from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    ACC_CHOICES = [
        ('INDIVISUAL','Indivisual'),
        ('TEAM','Team')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    acc_type = models.CharField(
        max_length = 10,
        choices = ACC_CHOICES,
        default = 'INDIVISUAL',
    )
    def __str__( self ):
        return self.user.username