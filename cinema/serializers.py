from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import APIException
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


class SeatToReserveSerializer(ModelSerializer):
    class Meta:
        model = SeatToReserve
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        # reservation_type_id = ReservationType.objects.get(
        #     name=validated_data["reservation_type"]
        # ).id
        #
        # res = Reservation.objects.create(
        #     screening_id=validated_data["screening_id"],
        #     reservation_type=reservation_type_id,
        #     paid=False,
        #     active=True
        # )
        # t = Ticket.objects.create(
        #     reservation_id=res.id,
        #     screening_id=validated_data["screening_id"],
        #     client_id=self.context.get('request', None).user
        # )
        #
        # for seat in validated_data["seats"]:
        #     print(seat)
        #     if seat.reserved:
        #         self.set_reserved_exception(seat.seat_id)
        #     else:
        #         s = SeatToReserve.objects.create(
        #             seat_id=seat.id,
        #             reservation_id=res.id,
        #             screening_id=validated_data["screening_id"],
        #             reserved=True
        #         )
        #         t.seats.add(s)
        #
        # t.save()

    def set_reserved_exception(self, seat):
        raise APIException(f"Seat {seat} already reserved!")
