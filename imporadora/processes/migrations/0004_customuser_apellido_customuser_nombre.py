# Generated by Django 5.0.6 on 2024-06-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0003_customuser_direccion_customuser_rut_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
