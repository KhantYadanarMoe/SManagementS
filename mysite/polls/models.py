from django.db import models

class Polls(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fathername = models.CharField(max_length=255)
  dateofbirth = models.CharField(max_length=255)
  nrcno = models.CharField(max_length=255)
  contactno = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  pAddress = models.CharField(max_length=255)
  edu = models.CharField(max_length=255)
  job = models.CharField(max_length=255)
