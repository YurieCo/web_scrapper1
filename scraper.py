# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
# from requests_html import HTMLSession
# import scraperwiki
# base_url = ' https://www.zomato.com/melbourne/dinner-in-ashburton'

# headers = {
#     "Host": "www.zomato.com",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# "Accept-Language": "en-GB,en;q=0.5",
# "Accept-Encoding": "gzip, deflate, br",
# "Connection": "keep-alive",
# "Upgrade-Insecure-Requests": "1"
# }

# session = HTMLSession()
# r = session.get(base_url, headers = headers)
# r.html.render()
# print(r.ok, r.status_code)


import scraperwiki

# Blank Python

import scraperwiki
import lxml.html

URL = "http://www.edikte.justiz.gv.at/edikte/ex/exedi3.nsf/suche?OpenForm&subf=v&query=%5BBL%5D%3D5"

web_page = lxml.html.parse(URL)

table_of_insolvencies = web_page.find('//table/tbody')

for row in table_of_insolvencies.findall('tr'):
    cells = row.findall('td')
    nr, type, adresse , objektbezeichnung,  = cells
    
    data = {}

    details_link = type.find('a')
    data['reference'] = details_link.text
    data['link'] = details_link.get('href')
    data['adresse _name'] = adresse.text

    remaining_lines = [d.tail for d in adresse .findall('br')]
    if len(remaining_lines) == 2:
        data['adresse _postcode'] = remaining_lines[0]
        data['adresse _town'] = remaining_lines[1]
    else:
        data['adresse _town'] = remaining_lines[0] 

    data['adresse _postcode'], data['adresse _town'] = data['adresse _town'].split(" ", 1)
    
    scraperwiki.sqlite.save(unique_keys=['reference'], data=data)
