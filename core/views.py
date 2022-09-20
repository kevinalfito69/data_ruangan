
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# generate pdf data barang
from django.http import FileResponse
import io
from .models import (data_barang, pegawai)
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


@login_required(login_url='/admin/')
def databarang_pdf(request):
    template_path = 'data_barang.html'
    data = data_barang.objects.all()

    context = {'myvar': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_barang.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url='/admin/')
def datapegawai_pdf(request):
    template_path = 'data_pegawai.html'
    data = pegawai.objects.all()

    context = {'myvar': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_pegawai.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def index(request):

    return render(request, "index.html",)


@login_required(login_url='/admin/')
def pdfViews(request):
    return render(request, 'import.html')
