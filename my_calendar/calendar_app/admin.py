from django.contrib import admin

from .models import *


class MonthAdmin(admin.ModelAdmin):
    model = Month
    list_display = ('id', 'title_month', 'amount_of_days', 'number_of_the_month')
    list_display_links = ('id', 'title_month', 'amount_of_days', 'number_of_the_month')
    search_fields = ('id', 'title_month', 'amount_of_days', 'number_of_the_month')


class WeekAdmin(admin.ModelAdmin):
    model = Week
    list_display = ('id', 'title_week', 'number_of_the_week')
    list_display_links = ('id', 'title_week', 'number_of_the_week')
    search_fields = ('id', 'title_week', 'number_of_the_week')


admin.site.register(Month, MonthAdmin)
admin.site.register(Week, WeekAdmin)
