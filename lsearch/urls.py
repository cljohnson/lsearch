from django.conf.urls import patterns, include, url
from goodsoul_scraper import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # 
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/', 'goodsoul_scraper.views.home', name='home'),
    url(r'^goodsoul_scrape/', 'goodsoul_scraper.views.goodsoul_scrape', name='goodsoul_scrape'),
)
