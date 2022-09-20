from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('import/', views.pdfViews, name='import'),
    path('databarang_pdf/', views.databarang_pdf, name='databarang_pdf'),
    path('datapegawai_pdf/', views.datapegawai_pdf, name='datapegawai_pdf'),
]
