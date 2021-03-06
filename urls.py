from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'directory.views.home', name='home'),
    # url(r'^directory/', include('directory.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^ajax_filtered_fields/', include('ajax_filtered_fields.urls')),

    (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    #ajax stuff
    (r'^ajax/client/simple_city$', 'itputils.views.city_value_ajax_servant'),
    (r'^ajax/client/country$', 'itputils.views.country_city_ajax_servant'),
    (r'^ajax/client/industry$', 'itpdirectory.views.industry_ajax_servant'),
    (r'^ajax/client/company_directory_many$', 'itpdirectory.views.company_directory_many_ajax_servant'),

)
