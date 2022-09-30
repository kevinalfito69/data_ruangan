from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('import/', views.pdfViews, name='import'),
    path('databarang_pdf/', views.datadokumen_pdf, name='databarang_pdf'),
    path('datapegawai_pdf/', views.datapegawai_pdf, name='datapegawai_pdf'),
    path('datamasuk_pdf/', views.datamasuk_pdf, name='datamasuk_pdf'),
    path('datakeluar_pdf/', views.datakeluar_pdf, name='datakeluar_pdf'),
]
