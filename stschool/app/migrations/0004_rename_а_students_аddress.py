# Generated by Django 4.2.3 on 2023-09-29 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_remove_students_аddress"),
    ]

    operations = [
        migrations.RenameField(
            model_name="students",
            old_name="А",
            new_name="Аddress",
        ),
    ]
