# Generated by Django 3.0.3 on 2020-02-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abogado', '0002_persona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abogado',
            name='id',
        ),
        migrations.AlterField(
            model_name='abogado',
            name='documento',
            field=models.FloatField(primary_key=True, serialize=False),
        ),
    ]