from django.shortcuts import render
from rest_framework.response import Response 

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
# Create your views here.

def hello(request):
    return render(request,'reports/demo.html')

def link_callback(uri, rel):
    import os
    from django.conf import settings
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    from django.contrib.staticfiles import finders
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    return path

def html2pdf(request):
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    _template = 'reports/demo.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(_template)
    html = template.render()

    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback
        )
    if pisa_status.err:
        return Response(status=500, data="error generating pdf")
    return response


def html2pdf1(request):
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    _template = 'reports/demo1.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(_template)
    html = template.render()

    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback
        )
    if pisa_status.err:
        return Response(status=500, data="error generating pdf")
    return response

def html2pdf2(request):

    headers = ["a", "b", "c", "d", "e", "f"]
    data = [20, 30, 40, 50, 60, 60]

    context = {
        "headers": headers,
        "data": data
    }

    from django.template.loader import get_template
    from xhtml2pdf import pisa
    _template = 'reports/demo2.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(_template)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback
        )
    if pisa_status.err:
        return Response(status=500, data="error generating pdf")
    return response

def export_pdf(request):
    
    context = {}
    html = render_to_string('reports/demo.html', context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"
    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response