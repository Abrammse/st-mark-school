# Generated by Django 4.2.3 on 2023-07-13 20:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="header",
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
                ("foot_sub", ckeditor.fields.RichTextField()),
                ("foot_title", ckeditor.fields.RichTextField()),
            ],
        ),
    ]
