from django.contrib import admin

from .models import (
    Cinema,
    Auditorium,
    Seat,
    SeatToReserve,
    Screening,
    ScreeningPrice,
    Reservation,
    ReservationType,
    Movie,
    Genre,
    Ticket,
)

admin.site.register(Cinema)
admin.site.register(Auditorium)
admin.site.register(Seat)
admin.site.register(SeatToReserve)
admin.site.register(Screening)
admin.site.register(ScreeningPrice)
admin.site.register(Reservation)
admin.site.register(ReservationType)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Ticket)
