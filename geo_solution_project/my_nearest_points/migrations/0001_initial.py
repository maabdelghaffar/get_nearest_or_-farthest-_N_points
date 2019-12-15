# Generated by Django 3.0 on 2019-12-14 23:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('x', models.DecimalField(decimal_places=2, max_digits=10)),
                ('y', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=3857)),
            ],
        ),
    ]
