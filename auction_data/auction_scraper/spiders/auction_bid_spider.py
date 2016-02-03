from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import replace_escape_chars

from auction_scraper.items import BidItems
from auction_bid_fields import auction_bid_fields

class AuctionBidsSpider(CrawlSpider):
    name = "auction_bids"
    allowed_domains = ["kvd.se"]
    start_urls = ["https://www.kvd.se/avslutade/personbil"]
    pipelines = ['bidpipeline']
 
    bid_list_xpath = '//div[@class="col item-content-compact"]' 

    rules = (Rule(LinkExtractor(allow=r'/?page=\d+',
    restrict_xpaths='//nav[@class="pagination"]/div[@class="item-list"]/ul/li'),
    follow = True),
    Rule(LinkExtractor(allow=r'/?page=\d+'),
    callback='parse_bids'))
         
    def parse_bids(self, response):
        
        selector = Selector(response)
        
        for bid in selector.select(self.bid_list_xpath) :
            loader = ItemLoader(BidItems(), selector=bid)

            loader.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
            loader.default_output_processor = Join()
       
            for field, xpath in auction_bid_fields.iteritems():
                loader.add_xpath(field, xpath)        

              
            yield loader.load_item()
  
