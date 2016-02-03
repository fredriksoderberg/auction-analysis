from sqlalchemy.orm import sessionmaker
from models import AuctionItem, BidItem, create_table
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

import settings

class AuctionPipeline(object):
    def __init__(self):
        engine = create_engine(URL(**settings.DATABASE))
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        
    def process_item(self, item, spider):
        if 'auctionpipeline' not in getattr(spider, 'pipelines') :
            return item

        session = self.Session()
        auction =  AuctionItem(**item)
        
        try:
            session.merge(auction)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
            
        return item

class BidPipeline(object):
     def __init__(self):
        engine = create_engine(URL(**settings.DATABASE))
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

     def process_item(self, item, spider):
        if 'bidpipeline' not in getattr(spider, 'pipelines') :
            return item

        session = self.Session()
        bid = BidItem(**item)
        
        try:
            session.merge(bid)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
            
        return item