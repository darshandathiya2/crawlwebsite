import scrapy
from ..items import CrawlwebsiteItem

class crawlSpider(scrapy.Spider):
    name = 'crawlwebsite'
    start_urls = [
        'https://www.imdb.com/list/ls002913270/'
    ]

    def parse(self, response):
        items = CrawlwebsiteItem()

        div_crawlwebsite = response.css('div.mode-detail')
        for crawlwebsite in div_crawlwebsite :
            actor_name =crawlwebsite.css('.lister-item-header a::text')[0].extract().strip()
            actor_name = [actor_name]
            personality = crawlwebsite.css('.text-small+ p::text')[0].extract().strip()
            personality = [personality]
            actor_image = crawlwebsite.css('img').xpath('@src').extract()
            items['actor_name'] = actor_name
            items['personality'] = personality
            items['actor_image'] = actor_image

            yield items

