from scrapy.item import Item, Field

class AuctionItems(Item):
    object_number = Field()
    auction_URL = Field()
    
    # auction info
    car_model = Field()
    description = Field()
    place_of_sale = Field()
    estimated_auction_price = Field()
    estimated_dealership_price = Field()
    buyer_fee = Field()
    auction_start = Field()

    # general info
    examiner_comment = Field()
    equipment = Field()
    registration_number = Field()
    model_year = Field()
    milage = Field()
    manufactured_date = Field()
    first_time_in_traffic = Field()
    service_book = Field()
    transmission = Field()
    nr_of_seats = Field()
    color = Field()
    car_paint = Field()
    fabric = Field()
    new_car_warranty = Field()
    car_damage_warranty = Field()

    # technical condition
    condition_technical_major_notes = Field()
    condition_technical_other_notes = Field()
    condition_technical_engine = Field()    
    condition_technical_transmission = Field()
    condition_technical_brakes = Field()
    condition_technical_service_history = Field()
    
    # misc condition
    misc_condition_major_notes = Field()
    misc_condition__other_notes = Field()
    misc_condition_body = Field()
    misc_condition_interior = Field()

    # Tyres and rims
    tyres_current_type = Field()
    rims_current_type = Field()
    tyres_current_condtion_front = Field()
    tyres_current_condtion_back = Field()
    tyres_extra_type = Field()
    rims_extra_type = Field()
    tyres_extra_condtion_front = Field()
    tyres_extra_condtion_back = Field()

    # technical data
    chassi_number = Field()
    first_registration = Field()
    vehicle_year = Field()
    nr_of_passengers = Field()
    engine_effect_kw = Field()
    engine_effect_hp = Field()
    fuel_type = Field()
    tow_hook = Field()
    max_load = Field()
    trailer_weight_b_card = Field()
    fuel_consumption = Field()
    co2_transmission = Field()
    service_period = Field()
    service_weight = Field()
    latest_examination = Field()
    taxation_yearly = Field()
    taxation_weight = Field()
    tow_weight = Field()
    total_weight = Field()

    # other info
    removable_VAT = Field()
    seller_type = Field()
    export_allowed = Field()
    new_car_price = Field()
    nr_of_keys = Field()
    import_type = Field()
    
    
class BidItems(Item) :
    object_number = Field()
    auction_date = Field()
    bidder = Field()
    highest_bid = Field()
