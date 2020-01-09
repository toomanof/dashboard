from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views


app_name = 'localset'

urlpatterns = [
    path('online/all_host/',
         login_required(views.OnLineHost.as_view()), name='online_host'),
    path('reg_hosts/',
         login_required(views.RegisteredHostView.as_view()), name='reg_hosts'),
]
