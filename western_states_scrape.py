#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:07:31 2021

@author: steph
"""
from urllib.request import urlopen # import urlopen to grab HTML from site
from urllib.error import HTTPError # import for HTTP error handling
from urlib.error import URLError # import for URL error handling
from bs4 import BeautifulSoup # import beautifulsoup for organizing HTML
import re # regular expressions

def getResults(url): # get the title for page to use later
    try: 
        html = urlopen('https://www.wser.org{}'.format(url)) # grabbing from western states site
    
    except HTTPError as e: # handling 404 or 500 errors
        print (e)
    
    except URLError:
        print('The srver could not be found.') # handling URL errors - if site down or URL is mistyped

    try: #program continues if no 404/ 500 error
        bs = BeautifulSoup(html, 'lxml') # making all the HTML on the site a bs object
        for link in bs.find('div', {'class':'entry'}).find_all(
            'a', href=re.compile('^(/results/)') # left off here
            # using reg ex to find all pages that finish with '/results/[year]-results/'
                                                             
        
        
    
   # except AttributeError: # handle unfound/ mistyped attribute tag errors
        #return None