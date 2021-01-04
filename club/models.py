from django.db import models

# Create your models here.


class Club_model(models.Model):
    club_name = models.CharField(max_length=50)


