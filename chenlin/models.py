from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class WorkInfo(models.Model):
    name = models.CharField(max_length=200)
    serial_num = models.CharField(max_length=200)
    remark = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class WorkPic(models.Model):
    work_info = models.ForeignKey(WorkInfo, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos')

