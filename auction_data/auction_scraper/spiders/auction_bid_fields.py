auction_bid_fields = {
        'object_number': './/div[@class="col item-id-closed"]/p/text()',
        'auction_date' : './/div[@class="col item-date-closed"]/p/text()',
        'bidder' : './/div[@class="col item-user-closed"]/p/text()',
        'highest_bid' : './/div[@class="col item-bid-compact"]/p/span/text()'
}