from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import replace_escape_chars

from auction_scraper.items import AuctionItems
from auction_item_fields import auction_item_fields

class AuctionItemspider(CrawlSpider):
    name = "auction_items"
    allowed_domains = ["kvd.se"]
    start_urls = ["https://www.kvd.se/auktion/personbil/"]
    pipelines = ['auctionpipeline']

    rules = (Rule(LinkExtractor(allow=r'/?page=\d+',
    restrict_xpaths='//nav[@class="pagination"]/div[@class="item-list"]/ul/li'),
    follow = True),
    Rule(LinkExtractor(allow=r'^https://www.kvd.se/auktion/personbil/.+/.+/\d+$'),
    callback='parse_auction_item'))
         
    def parse_auction_item(self, response):
        
        loader = ItemLoader(AuctionItems(), response=response)

        loader.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
        loader.default_output_processor = Join()
       
        for field, xpath in auction_item_fields.iteritems():
            loader.add_xpath(field, xpath)        

              
        yield loader.load_item()
