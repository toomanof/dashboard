"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include('apps.dashboard.urls', namespace="dashboard")),
    path('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('localset/', include('apps.localset.urls',
                              namespace="localset")),
    path('company/', include('apps.company.urls',
                             namespace="company")),
]


urlpatterns += [
    path('api/auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('api/company/', include('apps.company.api_urls',
                                 namespace="api_company")),
    path('api/localset/', include('apps.localset.api_urls',
                                  namespace="api_localset")),
    path('select2/', include('django_select2.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
