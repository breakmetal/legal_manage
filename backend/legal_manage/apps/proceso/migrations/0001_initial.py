# Generated by Django 3.0.3 on 2020-02-06 23:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abogado', '0002_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=60)),
                ('mensaje', models.CharField(max_length=100)),
                ('expedicion', models.DateTimeField()),
                ('limite', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('radicado', models.FloatField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('JURIDICO', 'juridico'), ('OTRO', 'otro')], default='JURIDICO', max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=150)),
                ('fecha_providencia', models.DateTimeField()),
                ('fecha_publicacion', models.DateTimeField()),
                ('fecha_finalizacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Notificados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificado', models.BooleanField(default=False)),
                ('medio', models.CharField(choices=[('EMAIL', 'email'), ('PERSONAL', 'personal'), ('TELEFONO', 'telefono')], default='EMAIL', max_length=30)),
                ('notificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proceso.Notificacion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abogado.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='notificacion',
            name='proceso',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proceso.Proceso'),
        ),
        migrations.CreateModel(
            name='Ejecutivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pretencion', models.FloatField()),
                ('titulo', models.CharField(choices=[('VALOR', 'valor'), ('EJECUTIVO', 'ejecutivo')], default='VALOR', max_length=9)),
                ('obligacion', models.CharField(choices=[('DAR', 'dar'), ('HACER', 'hacer'), ('NO_HACER', 'no hacer')], default='DAR', max_length=8)),
                ('cuantia', models.CharField(default='minima', max_length=6)),
                ('proceso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proceso.Proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Cautelar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(choices=[('REALES', 'reales'), ('BANCARIAS', 'bancarias'), ('DINEARIAS', 'dinearias'), ('DOCUMENTALES', 'documentales')], default='REALES', max_length=15)),
                ('estado', models.CharField(choices=[('ORDENACION', 'ordenacion'), ('CONSTITUCION', 'constitucion'), ('CLASIFICACION', 'clasificacion'), ('CANCELACION', 'cancelacion'), ('ACEPTADO', 'aceptado')], default='ORDENACION', max_length=15)),
                ('secuestro_info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('proceso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proceso.Proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('IMAGENES', 'imagenes'), ('PDF', 'pdf'), ('WORD', 'word')], default=(('IMAGENES', 'imagenes'), ('PDF', 'pdf'), ('WORD', 'word')), max_length=15)),
                ('documento', models.CharField(max_length=30)),
                ('extencion', models.CharField(max_length=10)),
                ('ruta', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('proceso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proceso.Proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Actuacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actuacion', models.CharField(max_length=60)),
                ('Anotacion', models.CharField(max_length=100)),
                ('inicio', models.DateTimeField()),
                ('termino', models.DateTimeField()),
                ('registro', models.DateTimeField()),
                ('proceso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proceso.Proceso')),
            ],
        ),
    ]
