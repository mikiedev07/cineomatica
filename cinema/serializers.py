from rest_framework.serializers import ModelSerializer
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


class CinemaSerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class AuditoriumSerializer(ModelSerializer):
    class Meta:
        model = Auditorium
        fields = '__all__'


class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReservationTypeSerializer(ModelSerializer):
    class Meta:
        model = ReservationType
        fields = '__all__'


class ScreeningPriceSerializer(ModelSerializer):
    class Meta:
        model = ScreeningPrice
        fields = '__all__'


class ScreeningSerializer(ModelSerializer):
    class Meta:
        model = Screening
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class SeatReservedSerializer(ModelSerializer):
    class Meta:
        model = SeatReserved
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
