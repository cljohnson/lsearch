from django.contrib import admin

# Register your models here.
from goodsoul_scraper.models import *
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Person)
admin.site.register(GoodsoulPage)