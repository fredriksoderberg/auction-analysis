BOT_NAME = 'auction_bot'
SPIDER_MODULES = ['auction_scraper.spiders']
DATABASE = {
    'drivername' : 'postgresql',
    'host' : 'localhost',
    'port' : '5432',
    'username' : 'postgres',
    'password' : 'postgres',
    'database' : 'kvd_auctions'
}
ITEM_PIPELINES = {
    'auction_scraper.pipelines.AuctionPipeline': 300,
    'auction_scraper.pipelines.BidPipeline' : 400 
} 
DOWNLOAD_HANDLERS = {'s3': None}
RANDOMIZE_DOWNLOAD_DELAY = True