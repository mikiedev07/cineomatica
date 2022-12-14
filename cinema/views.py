from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

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
    SeatToReserve,
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
    SeatToReserveSerializer,
    TicketSerializer,
)


class CinemaViewSet(ModelViewSet):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    permission_classes = [AllowAny]


class AuditoriumViewSet(ModelViewSet):
    serializer_class = AuditoriumSerializer
    queryset = Auditorium.objects.all()
    permission_classes = [AllowAny]


class SeatViewSet(ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()
    permission_classes = [AllowAny]


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsAdminUser]


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [AllowAny]


class ReservationTypeViewSet(ModelViewSet):
    serializer_class = ReservationTypeSerializer
    queryset = ReservationType.objects.all()
    permission_classes = [IsAdminUser]


class ScreeningPriceViewSet(ModelViewSet):
    serializer_class = ScreeningPriceSerializer
    queryset = ScreeningPrice.objects.all()
    permission_classes = [IsAdminUser]


class ScreeningViewSet(ModelViewSet):
    serializer_class = ScreeningSerializer
    queryset = Screening.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = [IsAdminUser]


class SeatToReserveViewSet(ModelViewSet):
    serializer_class = SeatToReserveSerializer
    queryset = SeatToReserve.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
