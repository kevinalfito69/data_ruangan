from django.contrib import admin
from .models import (pegawai, masuk, keluar, data_dokumen)
# Register your models here.


class masuk_admin(admin.ModelAdmin):
    readonly_fields = ["tanggal_masuk"]
    fieldsets = (
        ("general", {"fields": ("id_pegawai", "kegiatan", "pinjam_dokumen")}),
        ("time", {"fields": ["jam_masuk", "tanggal_masuk"]}),
    )


class keluar_admin(admin.ModelAdmin):
    readonly_fields = ["tanggal_keluar"]


admin.site.register(pegawai)
admin.site.register(data_dokumen)
admin.site.register(masuk, masuk_admin)
admin.site.register(keluar, keluar_admin)
