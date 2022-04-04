import scrapy
from demo_project.items import techItem
from demo_project.items import footballItem
from demo_project.items import cricketItem
from demo_project.items import newsItem
from scrapy.loader import ItemLoader

class techSpider(scrapy.Spider):
    name= "tech"

    start_urls=['https://www.theverge.com/tech']
    def parse(self,response):
        for tnews in response.xpath("//div[@class='c-entry-box--compact c-entry-box--compact--article']"):
            l=ItemLoader(item=techItem(),selector=tnews)
            l.add_xpath('tech_news', ".//div[@class='c-entry-box--compact__body']/h2")
            yield l.load_item()

class footballSpider(scrapy.Spider):
    name= "football"

    start_urls=['https://www.espn.in/football/']
    def parse(self,response):
        for fnews in response.xpath("//div[@class='contentItem__contentWrapper']"):
            l=ItemLoader(item=footballItem(),selector=fnews)
            l.add_xpath('football_news', ".//div[@class='contentItem__titleWrapper']/h1")
            yield l.load_item()
class cricketSpider(scrapy.Spider):
    name= "cricket"

    start_urls=['https://www.espn.in/cricket/']
    def parse(self,response):
        for cnews in response.xpath("//div[@class='contentItem__contentWrapper']"):
            l=ItemLoader(item=cricketItem(),selector=cnews)
            l.add_xpath('cricket_news', ".//div[@class='contentItem__titleWrapper']/h1")
            yield l.load_item()
class newsSpider(scrapy.Spider):
    name= "news"

    start_urls=['https://www.reuters.com/news/archive/worldNews']
    def parse(self,response):
        for topnews in response.xpath("//article"):
            l=ItemLoader(item=newsItem(),selector=topnews)
            l.add_xpath('top_news', ".//div[@class='story-content']/a/h3")
            yield l.load_item()