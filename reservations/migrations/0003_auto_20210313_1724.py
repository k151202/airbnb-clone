# Generated by Django 2.2.5 on 2021-03-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20210313_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedday',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
