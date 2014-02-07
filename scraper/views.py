import os
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
# Create your views here.
def home(request):
    return (HttpResponse("<h1><a href='/home/'>Home</a></h1>This project is about a lot of things - mostly learning things right now - things that will be applied to building things soon!"))
	
def scrape(request):
    page = urllib2.urlopen('http://www.goodsoul.us/wordpress/?page_id=2132')
    soup = BeautifulSoup(page)
    body_texts = soup.body(text=True)
    not_blank = 0
    this_page = []
    txt = ""
    start_record = 0
    reps = {'&#8220;':'"', '&#8221;':'"', '&#8250':'>'}
    for part in range(0, len(body_texts)):
        thispart = body_texts[part]
        if thispart != "":
            if start_record == 1:
                txt = txt + thispart + "\n"
            if thispart.find('#header') > 0:
                start_record = 1
            if thispart.find('#post') > 0:
			    start_record = 0
    html = replace_all(txt, reps)
    context = RequestContext(request)
    context_dict = {'html': html}
    return render_to_response('scraper/scrape_html.html', context_dict, context)
def replace_all(text, dic):
	for i, j in dic.iteritems():
		text = text.replace(i, j)
	return text