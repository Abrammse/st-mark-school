# Generated by Django 4.2.3 on 2023-07-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("new2", "0005_rename_address_student_addres_alter_student_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.FileField(default=2, upload_to="media/"),
            preserve_default=False,
        ),
    ]
