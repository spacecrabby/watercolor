from django.conf.urls import include, url
from django.contrib import admin
from landing import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'watercolor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.landing, name='landing'),
]
