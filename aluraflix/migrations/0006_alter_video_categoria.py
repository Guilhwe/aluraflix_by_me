# Generated by Django 5.0.3 on 2024-09-12 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0005_alter_video_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aluraflix.categoria1'),
        ),
    ]
