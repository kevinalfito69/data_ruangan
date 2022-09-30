
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# generate pdf data barang
from django.http import FileResponse
import io
from .models import (data_dokumen, pegawai, masuk, keluar)
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# data dokumen


@login_required(login_url='/admin/')
def datadokumen_pdf(request):
    template_path = 'data_dokumen.html'
    data = data_dokumen.objects.all()

    context = {'myvar': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_dokumen.pdf"'
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

# data pegawai pdf


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

# data masuk pdf


@login_required(login_url='/admin/')
def datamasuk_pdf(request):
    template_path = 'data_masuk.html'
    data = masuk.objects.all()

    context = {'myvar': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_masuk.pdf"'
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
# data pegawai pdf


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

# data keluar pdf


@login_required(login_url='/admin/')
def datakeluar_pdf(request):
    template_path = 'data_keluar.html'
    data = keluar.objects.all()

    context = {'myvar': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_keluar.pdf"'
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
