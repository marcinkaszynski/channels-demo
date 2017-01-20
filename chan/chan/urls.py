from django.conf.urls import url
from django.contrib import admin

from .counter.views import counter_view

urlpatterns = [
    url(r'^$', counter_view),
    url(r'^admin/', admin.site.urls),
]
