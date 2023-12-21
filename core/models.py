from email.policy import default
from enum import auto
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models

# Create your models here.


class pegawai(models.Model):
    kelamin = (
        ('Laki-laki', 'laki-laki'),
        ('Prempuan', 'prempuan'),
    )
    id_pegawai = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(choices=kelamin, max_length=10)

    def __str__(self):
        return ("({}) {}").format(self.id_pegawai, self.nama)

    class Meta:

        verbose_name_plural = "Pegawai"


class masuk(models.Model):
    id_pegawai = models.ForeignKey("pegawai", on_delete=models.CASCADE)
    kegiatan = models.CharField(max_length=200)
    tanggal_masuk = models.DateField(auto_now_add=True)
    jam_masuk = models.TimeField()
    pinjam_dokumen = models.ForeignKey(
        "data_dokumen", on_delete=models.CASCADE)

    def __str__(self):
        return ("{}, {},{}").format(self.id_pegawai, self.pinjam_dokumen, self.jam_masuk)
    class Meta:
        verbose_name_plural = "Data masuk Ruangan"
@receiver(post_save, sender=masuk)
def update_jumlah_exemplar(sender, instance, **kwargs):
    if instance.pinjam_dokumen:
        dokumen = instance.pinjam_dokumen
        if dokumen.jumlah_exemplar > 0:
            dokumen.jumlah_exemplar -= 1
            dokumen.save()

class keluar(models.Model):
    data_peminjam = models.ForeignKey(
        "masuk", on_delete=models.CASCADE, blank=True, null=True)
    tanggal_keluar = models.DateField(auto_now_add=True)
    jam_keluar = models.TimeField()

    def __str__(self):
        return ("{}, {}").format(self.data_peminjam, self.tanggal_keluar)

    class Meta:

        verbose_name_plural = "Data keluar Ruangan"
@receiver(post_save, sender=keluar)
def increase_exemplar_count(sender, instance, **kwargs):
    if instance.data_peminjam:
        dokumen = instance.data_peminjam.pinjam_dokumen
        if dokumen:
            dokumen.jumlah_exemplar += 1
            dokumen.save()


class data_dokumen(models.Model):
    nama_dokumen = models.CharField(max_length=200)
    jenis_dokumen = models.CharField(max_length=200)
    jumlah_exemplar = models.PositiveIntegerField(default=1)  # Field untuk jumlah salinan
    tanggal_ditambah = models.DateField()


    def __str__(self):
        return self.nama_dokumen

    class Meta:

        verbose_name_plural = "Data dokumen"
