import urllib.request,json
from .models import Sources,Articles
from datetime import datetime

#getting the api key
api_key = None

#getting the news base url
base_url = None

#getting the articlces url
articles_url = None

def configure_request(app):
    	global api_key,base_url,articles_url
	api_key = app.config['NEWS_API_KEY']
	base_url = app.config['NEWS_SOURCES_BASE_URL']
	articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
    	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results