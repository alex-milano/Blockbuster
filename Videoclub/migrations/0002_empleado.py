# Generated by Django 4.0 on 2022-01-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videoclub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]