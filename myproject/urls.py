from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'workshops.views.workshop', name='workshop'),
    url(r'^CX6AD3QrLgcFZu85GZmLMrY1PoKDU9S4pqlJHAnPhtU5CFpMur/', 'workshops.views.responses'),
    url(r'^CX6AD3QrLgcFZu85GZmLMrY1PoKDU9S4pqlJHAnPhtU5CFpMur/zip/', 'workshops.views.return_zipped_file'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
