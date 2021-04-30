from django.db import models

# Create your models here.

class Patient_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=200)
    mail = models.EmailField(default=None)
    xray_sheet = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    