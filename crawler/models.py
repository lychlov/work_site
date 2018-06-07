from django.db import models


# Create your models here.
class TargetMP(models.Model):
    target_mp_name = models.CharField(max_length=200)
