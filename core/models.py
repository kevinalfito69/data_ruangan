
from pyexpat import model
from django.db import models

# Create your models here.
class pegawai(models.Model):
    kelamin=(
        ('Laki-laki', 'laki-laki'),
        ('Prempuan', 'prempuan'),
    )
    id_pegawai = models.CharField( max_length=50)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(choices=kelamin, max_length=10)
    def __str__(self):
        return ("{}, {}").format(self.id_pegawai, self.nama)
    class Meta:
        
        verbose_name_plural = "Pegawai"

class report_in(models.Model):
    id_pegawai = models.ForeignKey("pegawai", on_delete=models.CASCADE)
    tujuan = models.CharField(max_length=200)
    tanggal_masuk = models.DateField(auto_now_add=True)
    pinjam_alat = models.ForeignKey("data_barang", on_delete=models.CASCADE)
    def __str__(self):
        return ("{}, {}").format(self.id_pegawai, self.pinjam_alat)
    class Meta:
        verbose_name_plural = "Report in"

class report_out(models.Model):
    data_peminjam = models.ForeignKey("report_in", on_delete=models.CASCADE, blank=True, null=True)
    tanggal_keluar = models.DateField(auto_now=True)
    def __str__(self):
        return ("{}, {}").format(self.data_peminjam, self.tanggal_keluar)
    class Meta:
        
        verbose_name_plural = "Report out"

class data_barang(models.Model):
    nama_barang = models.CharField(max_length=200)
    jumlah = models.IntegerField()
    tanggal_ditambah = models.DateField( auto_now=True)
    def __str__(self):
        return self.nama_barang
        
    class Meta:
        
        verbose_name_plural = "Data Barang"