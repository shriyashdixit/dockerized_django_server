from django.contrib import admin

# Register your models here.
from .models import HistoricalData, HistoricalDataNSE, LiveDataNSE


@admin.register(HistoricalData)
class HistoricalDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'open', 'high', 'low', 'close']


@admin.register(HistoricalDataNSE)
class HistoricalDataNSEAdmin(admin.ModelAdmin):
    list_display = ['date', 'open', 'high', 'low', 'close', 'adj_close', 'close']


@admin.register(LiveDataNSE)
class LiveDataNSEdmin(admin.ModelAdmin):
    list_display = ['ticker', 'date', 'price']
