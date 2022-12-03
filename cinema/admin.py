from django.contrib import admin

from .models import (
    Cinema,
    Auditorium,
    Seat,
    SeatReserved,
    Screening,
    ScreeningPrice,
    Reservation,
    ReservationType,
    Movie,
    Genre
)

admin.site.register(Cinema)
admin.site.register(Auditorium)
admin.site.register(Seat)
admin.site.register(SeatReserved)
admin.site.register(Screening)
admin.site.register(ScreeningPrice)
admin.site.register(Reservation)
admin.site.register(ReservationType)
admin.site.register(Movie)
admin.site.register(Genre)
