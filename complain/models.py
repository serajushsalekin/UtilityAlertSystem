from django.db import models


class ComplainBox(models.Model):
    fullname = models.CharField(max_length=100)
    postal = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    msg = models.TextField()

    def __str__(self):
        return self.fullname
