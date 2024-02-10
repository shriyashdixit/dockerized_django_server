from django.db import models

# Create your models here.


class HistoricalData(models.Model):
    date = models.DateTimeField('date published')
    open = models.DecimalField(max_digits=7, decimal_places=5)
    high = models.DecimalField(max_digits=7, decimal_places=5)
    low = models.DecimalField(max_digits=7, decimal_places=5)
    close = models.DecimalField(max_digits=7, decimal_places=5)


class HistoricalDataNSE(models.Model):
    ticker = models.CharField(max_length=50, default='null')
    date = models.DateTimeField('date published')
    open = models.DecimalField(max_digits=7, decimal_places=5)
    high = models.DecimalField(max_digits=7, decimal_places=5)
    low = models.DecimalField(max_digits=7, decimal_places=5)
    close = models.DecimalField(max_digits=7, decimal_places=5)
    adj_close = models.DecimalField(max_digits=7, decimal_places=5)
    volume = models.IntegerField(default=0)


class LiveDataNSE(models.Model):
    ticker = models.CharField(max_length=50, default='null')
    date = models.DateTimeField('date published')
    price = models.DecimalField(max_digits=9, decimal_places=3)
