# Generated by Django 4.1.2 on 2023-04-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gifts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Guests",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("number_of_guests", models.IntegerField(default=0)),
                ("message", models.TextField()),
            ],
        ),
    ]
