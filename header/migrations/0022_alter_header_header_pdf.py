# Generated by Django 4.2.2 on 2023-06-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("header", "0021_delete_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="header",
            name="header_pdf",
            field=models.FileField(blank=True, null=True, upload_to="header/"),
        ),
    ]