# Generated by Django 4.2.2 on 2023-07-02 17:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("header", "0026_alter_header_header_pr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="header",
            name="header_des",
            field=ckeditor.fields.RichTextField(),
        ),
    ]