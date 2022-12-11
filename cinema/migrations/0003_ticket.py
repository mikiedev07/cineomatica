# Generated by Django 4.1.3 on 2022-12-11 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0002_auditorium_genre_movie_reservation_reservationtype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.reservation')),
                ('seats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.seatreserved')),
            ],
        ),
    ]