#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:07:31 2021

@author: steph
"""
from urllib.request import urlopen # import urlopen to grab HTML from site
from urllib.error import HTTPError # import for HTTP error handling
from urllib.error import URLError # import for URL error handling
from bs4 import BeautifulSoup # import beautifulsoup to make order out of chaos aka HTML
import re # regular expressions

     
pages = set() # initially define pages as empty set 

def getLinks(url): # get links for all result pages and handle errors
    global pages
    
    try: 
        html = urlopen('https://www.wser.org/results/{}'.format(url)) # grabbing from western states site
        bs = BeautifulSoup(html, 'html.parser') # making all the HTML on the site as bs object
        for link in bs.find_all('a', href=re.compile('\/results\/\d\d\d\d-results')):  # using reg ex to find all pages that finish with '-results/'
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages: # encountering new page.
                    # adding new page link to pages if it has href attribute.
                    newPage = link.attrs['href']
                    print(newPage)
                    pages.add(newPage)          
                
    except HTTPError as e: # handling 404 or 500 errors
        print (e)
    
    except URLError:
        print('The srver could not be found.') # handling URL errors - if site down or URL is mistyped         
        
    
    
getLinks('') # calling with empty argument to start

                                                            
# def getResults( ):
    
# def writeResults( )
# will make excel file(s) Should I combine into one excel file? Probably easier.
# have to add column for year then.


