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
from users.models import Transaction


class CinemaSerializer(ModelSerializer):
    class Meta:
        model = Cinema
        fields = "__all__"


class AuditoriumSerializer(ModelSerializer):
    class Meta:
        model = Auditorium
        fields = "__all__"


class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ReservationTypeSerializer(ModelSerializer):
    class Meta:
        model = ReservationType
        fields = "__all__"


class ScreeningPriceSerializer(ModelSerializer):
    class Meta:
        model = ScreeningPrice
        fields = "__all__"


class ScreeningSerializer(ModelSerializer):
    class Meta:
        model = Screening
        fields = "__all__"

    def create(self, validated_data):
        sc = Screening.objects.create(
            auditorium_id=validated_data["auditorium_id"],
            movie_id=validated_data["movie_id"],
            start_time=validated_data["start_time"],
            price=validated_data["price"],
        )

        seats = Seat.objects.filter(auditorium_id=validated_data["auditorium_id"])
        for obj in seats:
            s = SeatToReserve.objects.create(seat_id=obj, screening_id=sc)
            s.save()

        return sc


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class SeatToReserveSerializer(ModelSerializer):
    class Meta:
        model = SeatToReserve
        fields = "__all__"


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

    def create(self, validated_data):
        user = self.context.get("request", None).user

        r_type = ReservationType.objects.get(name=validated_data["reservation_type"])

        res = Reservation.objects.create(
            screening_id=validated_data["screening_id"],
            reservation_type=r_type,
            paid=False,
            active=True,
        )

        t = Ticket.objects.create(
            reservation_id=res,
            screening_id=validated_data["screening_id"],
            client_id=user,
        )

        sp = ScreeningPrice.objects.get(reservation_type=r_type)
        no_disc_price = sp.price * len(validated_data["seats"])
        movie = validated_data["screening_id"].movie_id

        tr = Transaction.objects.create(
            reservation_id=res,
            client=user,
            total=no_disc_price - no_disc_price * user.discount / 100,
            discount=user.discount,
            movie_name=movie.name,
        )

        if user.has_card:
            user.discount += 3
        user.save()

        for seat in validated_data["seats"]:
            if seat.reserved is True:
                self.set_reserved_exception(seat)
                t.delete()
                return None
            else:
                t.seats.add(seat)
                seat.reserved = True
                seat.save()

        t.save()
        return t

    def set_reserved_exception(self, seat):
        raise APIException(f"Seat {seat} already reserved!")
