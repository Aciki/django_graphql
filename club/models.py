from django.db import models

# Create your models here.


class Club_model(models.Model):
    club_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.club_name


