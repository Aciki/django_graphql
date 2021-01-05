from django.db import models
from django.conf import settings

# Create your models here.
 
from club.models import Club_model


class P_info(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    date_of_birth = models.DateTimeField()
    height = models.SmallIntegerField()
    rating = models.IntegerField()
    is_available = models.BooleanField(default=True)
    club_name = models.ForeignKey(Club_model,on_delete=models.CASCADE)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.rating





   
