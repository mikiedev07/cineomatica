from rest_framework.viewsets import ModelViewSet

from .models import (
    Cinema,
    Auditorium,
    Seat,
    Genre,
    Movie,
    ReservationType,
    ScreeningPrice,
    Screening,
    Reservation,
    SeatReserved,
    Ticket,
)

from .serializers import (
    CinemaSerializer,
    AuditoriumSerializer,
    SeatSerializer,
    GenreSerializer,
    MovieSerializer,
    ReservationTypeSerializer,
    ScreeningPriceSerializer,
    ScreeningSerializer,
    ReservationSerializer,
    SeatReservedSerializer,
    TicketSerializer,
)


class CinemaViewSet(ModelViewSet):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class AuditoriumViewSet(ModelViewSet):
    serializer_class = AuditoriumSerializer
    queryset = Auditorium.objects.all()


class SeatViewSet(ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class ReservationTypeViewSet(ModelViewSet):
    serializer_class = ReservationTypeSerializer
    queryset = ReservationType.objects.all()


class ScreeningPriceViewSet(ModelViewSet):
    serializer_class = ScreeningPriceSerializer
    queryset = ScreeningPrice.objects.all()


class ScreeningViewSet(ModelViewSet):
    serializer_class = ScreeningSerializer
    queryset = Screening.objects.all()


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class SeatReservedViewSet(ModelViewSet):
    serializer_class = SeatReservedSerializer
    queryset = SeatReserved.objects.all()


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
