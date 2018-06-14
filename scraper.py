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
from requests_html import HTMLSession
import scraperwiki
base_url = ' https://www.zomato.com/melbourne/dinner-in-ashburton'

headers = {
    "Host": "www.zomato.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-GB,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
}

session = HTMLSession()
r = session.get(base_url, headers = headers)
r.html.render()
print(r.ok, r.status_code)

