# Generated by Django 4.2.2 on 2023-06-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("header", "0012_delete_day"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="header",
            name="header_image1",
        ),
        migrations.RemoveField(
            model_name="header",
            name="header_image2",
        ),
        migrations.AlterField(
            model_name="header",
            name="header_image",
            field=models.FileField(
                default=None, max_length=250, null=True, upload_to="header/"
            ),
        ),
    ]