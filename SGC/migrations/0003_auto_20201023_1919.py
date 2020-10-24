# Generated by Django 3.1.2 on 2020-10-24 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SGC', '0002_auto_20201005_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indicador',
            name='edicion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='procedimiento',
            name='creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procedimiento',
            name='edicion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='edicion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='creacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='edicion',
            field=models.DateField(auto_now=True),
        ),
    ]
