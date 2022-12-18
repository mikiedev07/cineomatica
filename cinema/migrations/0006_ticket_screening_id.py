# Generated by Django 4.1.3 on 2022-12-14 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0005_remove_ticket_seats_ticket_seats"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="screening_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="cinema.screening",
            ),
        ),
    ]
