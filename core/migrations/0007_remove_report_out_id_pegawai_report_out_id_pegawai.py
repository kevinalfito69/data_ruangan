# Generated by Django 4.1.1 on 2022-09-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_report_out_id_pegawai'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_out',
            name='id_pegawai',
        ),
        migrations.AddField(
            model_name='report_out',
            name='id_pegawai',
            field=models.ManyToManyField(to='core.report_in'),
        ),
    ]