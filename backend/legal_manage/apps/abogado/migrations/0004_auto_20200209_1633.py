# Generated by Django 3.0.3 on 2020-02-09 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abogado', '0003_auto_20200209_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='especialidad',
            field=models.CharField(default='555', max_length=50),
        ),
        migrations.AlterField(
            model_name='abogado',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='abogado',
            name='telefono',
            field=models.CharField(default='555', max_length=50),
        ),
    ]