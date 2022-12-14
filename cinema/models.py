from django.db import models


class Cinema(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	contacts = models.CharField(max_length=20)


class Auditorium(models.Model):
	name = models.TextField(max_length=30)
	cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)


class Seat(models.Model):
	row = models.IntegerField()
	number = models.IntegerField()
	auditorium_id = models.ForeignKey(Auditorium, on_delete=models.CASCADE)

	def __str__(self):
		return f"Row {self.row}, number {self.number}"


class Genre(models.Model):
	name = models.CharField(max_length=50)


class Movie(models.Model):
	name = models.CharField(max_length=50)
	release_date = models.DateField()
	age_limit = models.IntegerField()
	rental_start = models.DateField()
	rental_end = models.DateField()
	duration_min = models.IntegerField()
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	rating = models.FloatField()
	description = models.CharField(max_length=300)


class ReservationType(models.Model):
	name = models.CharField(max_length=20)


class ScreeningPrice(models.Model):
	reservation_type = models.ForeignKey(ReservationType, on_delete=models.CASCADE)
	price = models.FloatField()
	cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)


class Screening(models.Model):
	auditorium_id = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
	movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	price = models.ForeignKey(ScreeningPrice, on_delete=models.CASCADE)


class Reservation(models.Model):
	screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
	reservation_type = models.ForeignKey(ReservationType, on_delete=models.CASCADE)
	paid = models.BooleanField()
	active = models.BooleanField()


class SeatToReserve(models.Model):
	seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
	reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
	screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
	reserved = models.BooleanField(default=False)


class Ticket(models.Model):
	reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE, default=None)
	screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE, default=None)
	seats = models.ManyToManyField(SeatToReserve)
	client_id = models.ForeignKey('users.User', on_delete=models.CASCADE, default=None)
	reservation_type = models.CharField(max_length=5, default="adult")
