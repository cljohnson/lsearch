from django.conf.urls import patterns, include, url
from scraper import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # 
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/', 'scraper.views.home', name='home'),
    url(r'^scrape/', 'scraper.views.scrape', name='scape'),
)
