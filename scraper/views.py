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
	#hard code a page now - worry about how to dig through a site later
	#need to think about how to anticipate and reject extraneous content from daedal sites
    page = urllib2.urlopen('http://www.goodsoul.us/wordpress/?page_id=2132')
	#strip the page of its html
    soup = BeautifulSoup(page)
    body_texts = soup.body(text=True)
	####
	# special code to strip extraneous content i.e. the scrape pulls header, footer, menu content, as well as the post we want
	#     here we examine the content and look for key words - not something that would work well in the wild
	# we also find special entities that need to be converted
	# we also strip out blank lines
    not_blank = 0
    this_page = []
    txt = ""
    start_record = 0
	#dictionary of special html entities to be converted back to plain text - this can and should be generalized and included
    reps = {'&#8220;':'"', '&#8221;':'"', '&#8250':'>'}
	# perform the extraction
    for part in range(0, len(body_texts)):
        thispart = body_texts[part]
        if thispart != "":
            if start_record == 1:
                txt = txt + thispart + "\n"
            if thispart.find('#header') > 0:
                start_record = 1
            if thispart.find('#post') > 0:
			    start_record = 0
    #replace the special htm entities
	html = replace_all(txt, reps)
	#pass the results to a template
    context = RequestContext(request)
    context_dict = {'html': html}
    return render_to_response('scraper/scrape_html.html', context_dict, context)
#####
# helper functions not otherwise called directly by url
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text