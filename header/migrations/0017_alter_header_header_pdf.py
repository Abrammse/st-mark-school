# Generated by Django 4.2.2 on 2023-06-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("header", "0016_alter_header_header_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="header",
            name="header_pdf",
            field=models.FileField(default=2, max_length=1000, upload_to="header/"),
            preserve_default=False,
        ),
    ]