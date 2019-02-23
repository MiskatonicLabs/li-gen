from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.views.generic import TemplateView

from .models import License


class LicenseView(TemplateView):
    def get(self, request):
        return render(request, 'license/index.html', {'licenses': License.objects.all(), 'year': datetime.now().year})

    def post(self, request):
        license_template = Template(f'<pre>{License.objects.get(slug=request.POST["license"]).text}</pre>')
        context = Context({k: v for k, v in request.POST.items() if not k == 'license'})
        return HttpResponse(license_template.render(context))
