from django.contrib import admin
from .models import (pegawai, report_in, report_out, data_barang)
# Register your models here.
class reportin_admin(admin.ModelAdmin):
    readonly_fields = ["tanggal_masuk"]
class reportout_admin(admin.ModelAdmin):
     readonly_fields = ["tanggal_keluar"]
admin.site.register(pegawai)
admin.site.register(data_barang)
admin.site.register(report_in, reportin_admin)
admin.site.register(report_out,reportout_admin)
