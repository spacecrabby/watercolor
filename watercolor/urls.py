from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from landing import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'watercolor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.landing, name='landing'),
    url(r'^success', views.success, name='success'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
]
