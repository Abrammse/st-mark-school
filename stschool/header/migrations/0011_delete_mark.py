# Generated by Django 4.2.2 on 2023-06-30 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("header", "0010_remove_day_day_title"),
    ]

    operations = [
        migrations.DeleteModel(
            name="mark",
        ),
    ]