# Generated by Django 4.2.3 on 2023-07-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foot", "0004_rename_انكل_foot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foot",
            name="foot_sub",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="foot",
            name="foot_title",
            field=models.CharField(max_length=200),
        ),
    ]