BOT_NAME = 'auction_bot'
SPIDER_MODULES = ['auction_scraper.spiders']
ITEM_PIPELINES = {
    'auction_scraper.pipelines.AuctionPipeline': 300,
    'auction_scraper.pipelines.BidPipeline' : 400 
} 
DOWNLOAD_HANDLERS = {'s3': None}
RANDOMIZE_DOWNLOAD_DELAY = True