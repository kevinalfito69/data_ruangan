# Generated by Django 4.1.1 on 2022-09-30 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_keluar_jam_keluar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keluar',
            name='jam_keluar',
            field=models.TimeField(auto_now=True),
        ),
    ]
