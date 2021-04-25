# Generated by Django 3.2 on 2021-04-22 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_project", "0002_auto_20210422_1416"),
    ]

    operations = [
        migrations.AddField(
            model_name="homework",
            name="teacher_create_hw",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="my_project.teacher",
            ),
            preserve_default=False,
        ),
    ]
