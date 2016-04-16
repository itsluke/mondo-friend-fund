from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include('friendfund.urls')),
    url(r'^$', RedirectView.as_view(url='/v1/', permanent=True)),
]
