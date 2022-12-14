from rest_framework import routers
from django.urls import path

from .views import (
    CinemaViewSet,
    AuditoriumViewSet,
    SeatViewSet,
    GenreViewSet,
    MovieViewSet,
    ReservationViewSet,
    ScreeningPriceViewSet,
    ScreeningViewSet,
    ReservationTypeViewSet,
    SeatToReserveViewSet,
    TicketViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register('cinemas', CinemaViewSet)
router.register('auditoriums', AuditoriumViewSet)
router.register('seats', SeatViewSet)
router.register('genres', GenreViewSet)
router.register('movies', MovieViewSet)
router.register('reservations', ReservationViewSet)
router.register('prices', ScreeningPriceViewSet)
router.register('screenings', ScreeningViewSet)
router.register('reservation-types', ReservationTypeViewSet)
router.register('reserved-seats', SeatToReserveViewSet)
router.register('tickets', TicketViewSet)

urlpatterns = []

urlpatterns += router.urls
