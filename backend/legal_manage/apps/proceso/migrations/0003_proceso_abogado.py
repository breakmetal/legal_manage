# Generated by Django 3.0.3 on 2020-02-09 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abogado', '0004_auto_20200209_1633'),
        ('proceso', '0002_auto_20200209_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='abogado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abogado.Abogado'),
        ),
    ]
