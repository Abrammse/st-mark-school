# Generated by Django 4.2.2 on 2023-06-30 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("header", "0008_new"),
    ]

    operations = [
        migrations.CreateModel(
            name="day",
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
                ("day_sub", models.CharField(max_length=50)),
                ("day_title", models.CharField(max_length=50)),
            ],
        ),
    ]
