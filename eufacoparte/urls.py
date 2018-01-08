"""eufacoparte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.apps import apps
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import settings

from eufacopartesite.views import load_home


eufacosite_name = apps.get_app_config('eufacopartesite').verbose_name

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include("eufacopartesite.urls", namespace='eufacopartesite')),
    url(r'^', include(('eufacopartesite.urls', eufacosite_name), namespace='eufacosite')),
    # url(r'^eufaco/', load_home, name="home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)