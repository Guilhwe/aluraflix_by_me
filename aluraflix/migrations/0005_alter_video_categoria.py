# Generated by Django 5.0.3 on 2024-09-12 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0004_video_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aluraflix.categoria1'),
        ),
    ]
