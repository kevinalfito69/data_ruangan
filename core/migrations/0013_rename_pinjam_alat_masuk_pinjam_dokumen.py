# Generated by Django 4.1.1 on 2022-09-30 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_data_dokumen_options_alter_keluar_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masuk',
            old_name='pinjam_alat',
            new_name='pinjam_dokumen',
        ),
    ]
