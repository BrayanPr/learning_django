from django.urls import path, include

#views
from . import views as ReportViews

urlpatterns = [
    path('demo/', ReportViews.hello),
    path('pdf/', ReportViews.html2pdf),
    path('pdf1/', ReportViews.html2pdf1),
    path('pdf2/', ReportViews.html2pdf2),
    path('pdf3/', ReportViews.export_pdf),
]