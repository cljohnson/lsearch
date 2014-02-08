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
    #pass the results to a template
    context = RequestContext(request)
    html_head = 'This project is about a lot of things - mostly learning things right now - things that will be applied to building things soon!'
    goodsoul_scrape_link = '/goodsoul_scrape/goodsoul_scrape/'
    context_dict = {'html_head': html_head, 'goodsoul_scrape_link': goodsoul_scrape_link}
    return render_to_response('goodsoul_scraper/home.html', context_dict, context)
	
def goodsoul_scrape(request):
	#hard code a page now - worry about how to dig through a site later
	#need to think about how to anticipate and reject extraneous content from daedal sites
    page_id = '2340'
    page = urllib2.urlopen('http://www.goodsoul.us/wordpress/?page_id=' + page_id)
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
    reps = {'&#8220;':'"', '&#8221;':'"', '&#8217;':"'", '&#8250':'>', 'end of .post-entry':''}
	# perform the extraction
    for part in range(0, len(body_texts)):
        thispart = body_texts[part]
        if thispart != "":
            if start_record == 1:
                txt = txt + thispart + "\n"
            if thispart.find('#header') > 0:
                start_record = 1
            if thispart.find('end of .post-entry') > 0:
			    start_record = 0
    #replace the special htm entities
	html = replace_all(txt, reps)
	#pass the results to a template
    context = RequestContext(request)
    context_dict = {'html': html, 'page_id': page_id}
    return render_to_response('goodsoul_scraper/scrape.html', context_dict, context)
#####
# helper functions not otherwise called directly by url
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text