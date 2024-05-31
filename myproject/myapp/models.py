from django.db import models

class UploadData(models.Model):
  state = models.CharField(max_length=255)
  dpd = models.IntegerField()
  count = models.IntegerField()
