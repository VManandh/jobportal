from django.contrib import admin
from .models import *

class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company_name',
        'location',
        'experience',
        'salary',
        'posted_on'
    )

    list_filter = (
        'location',
        'experience',
        'posted_on'
    )

    search_fields = (
        'title',
        'company_name',
        'skills'
    )

    ordering = ('-posted_on',)

    readonly_fields = ('posted_on',)


# admin.site.register(Joblist, JobAdmin)

# admin.site.register(Joblist)

class messenger(admin.ModelAdmin):
    admin.site.register(Message)


# ====================================================================

from django.contrib import admin
from .models import EEmployerProfile, Job, Application

admin.site.register(EEmployerProfile)
admin.site.register(Job)
admin.site.register(Application)


# =================================================================
from django.contrib import admin
from .models import (
    Route,Bus, Seat,
    Trip,
    Booking
)
# admin.site.register(Route)
# admin.site.register(BusOperator)
# admin.site.register(Bus)
# admin.site.register(Seat)
# admin.site.register(Trip)
# admin.site.register(BoardingPoint)
# admin.site.register(DropPoint)
# admin.site.register(Booking)
# admin.site.register(Passenger)
# admin.site.register(Payment)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'destination')
    search_fields = ('source', 'destination')

admin.site.register(Route, RouteAdmin)
class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus_name', 'bus_number', 'total_seats')
    search_fields = ('bus_name', 'bus_number')

admin.site.register(Bus, BusAdmin)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'seat_number')
    list_filter = ('bus',)

admin.site.register(Seat, SeatAdmin)
class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'route', 'journey_date')
    list_filter = ('journey_date', 'route')

admin.site.register(Trip, TripAdmin)

