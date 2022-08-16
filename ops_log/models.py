from django.db import models

class CrossoutOperator(models.Model):
    crossout = models.CharField(max_length=100)
    operator = models.CharField(max_length=50)