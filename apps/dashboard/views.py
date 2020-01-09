from django.http import HttpResponse

from django.views.generic import TemplateView


# Create your views here.

def dashboard_index(request):
    return HttpResponse('Ok', status=200)


class IndexDashboard(TemplateView):
    template_name = 'index_dashboard.html'
