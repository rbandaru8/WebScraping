# This tells us about the scraping of sites (thru view source code). Some websites, doesn't want to scrape their content. For eg, sirbnb/robots.txt - will list of pages allow, disallow for certain bots - googlebot, bingbot.. 
https://www.airbnb.com/robots.txt - lists ethical ways of scraping content. 
Special site for developers: https://news.ycombinator.com/ 

Some websites, doesn't provide any APIs to expose their info. Then we can scrape their website and see if we can get the required information. 
We will use "Beautiful Soup" library for webscraping - https://pypi.org/project/beautifulsoup4/ 
pip install beautifulsoup4  -- isntall this lib
pip install requests  -- allows us to grab html files

-- Scrapy framework is also used to webscraping. https://scrapy.org/
pip install scrapy   -- not used in this project though. 