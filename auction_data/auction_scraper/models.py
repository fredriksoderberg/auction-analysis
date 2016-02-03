from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

DeclarativeBase = declarative_base()

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class AuctionItem(DeclarativeBase):
    __tablename__ = "kvd_auction_object"
    
    object_number = Column(Integer, primary_key = True)
    auction_URL = Column('auction_URL', String, nullable=True)
    
    # auction info
    car_model = Column('car_model', String, nullable=True)
    description =  Column('description', String, nullable=True)
    place_of_sale = Column('place_of_sale', String, nullable=True)
    estimated_auction_price = Column('estimated_auction_price', String, nullable=True)
    estimated_dealership_price = Column('estimated_dealership_price', String, nullable=True)
    buyer_fee = Column('buyer_fee', String, nullable=True)
    auction_start = Column('auction_start', String, nullable=True)
    
    # general info
    examiner_comment = Column('examiner_comment', String, nullable=True)
    equipment = Column('equipment', String, nullable=True)
    registration_number = Column('registration_number', String, nullable=True)
    model_year = Column('model_year', String, nullable=True)
    milage =Column('milage', String, nullable=True)
    manufactured_date = Column('manufactured_date', String, nullable=True)
    first_time_in_traffic = Column('first_time_in_traffic', String, nullable=True)
    service_book = Column('service_book', String, nullable=True)
    transmission = Column('transmission', String, nullable=True)
    nr_of_seats = Column('nr_of_seats', String, nullable=True)
    color = Column('color', String, nullable=True)
    car_paint = Column('car_paint', String, nullable=True)
    fabric = Column('fabric', String, nullable=True)
    new_car_warranty = Column('new_car_warranty', String, nullable=True)
    car_damage_warranty = Column('car_damage_warranty', String, nullable=True)

    # technical condition
    condition_technical_major_notes = Column('condition_technical_major_notes', String, nullable=True)
    condition_technical_other_notes = Column('condition_technical_other_notes', String, nullable=True)
    condition_technical_engine = Column('condition_technical_engine', String, nullable=True) 
    condition_technical_transmission = Column('condition_technical_transmission', String, nullable=True)
    condition_technical_brakes = Column('condition_technical_brakes', String, nullable=True)
    condition_technical_service_history = Column('condition_technical_service_history', String, nullable=True)
    
    # misc condition
    misc_condition_major_notes = Column('misc_condition_major_notes', String, nullable=True)
    misc_condition__other_notes = Column('misc_condition__other_notes', String, nullable=True)
    misc_condition_body = Column('misc_condition_body', String, nullable=True)
    misc_condition_interior = Column('misc_condition_interior', String, nullable=True)

    # Tyres and rims
    tyres_current_type = Column('tyres_current_type', String, nullable=True)
    rims_current_type = Column('rims_current_type', String, nullable=True)
    tyres_current_condtion_front = Column('tyres_current_condtion_front', String, nullable=True)
    tyres_current_condtion_back = Column('tyres_current_condtion_back', String, nullable=True)
    tyres_extra_type = Column('tyres_extra_type', String, nullable=True)
    rims_extra_type = Column('rims_extra_type', String, nullable=True)
    tyres_extra_condtion_front = Column('tyres_extra_condtion_front', String, nullable=True)
    tyres_extra_condtion_back = Column('tyres_extra_condtion_back', String, nullable=True)

    # technical data
    chassi_number = Column('chassi_number', String, nullable=True)
    first_registration = Column('first_registration', String, nullable=True)
    vehicle_year = Column('vehicle_year', String, nullable=True)
    nr_of_passengers = Column('nr_of_passengers', String, nullable=True)
    engine_effect_kw = Column('engine_effect_kw', String, nullable=True)
    engine_effect_hp = Column('engine_effect_hp', String, nullable=True)
    fuel_type = Column('fuel_type', String, nullable=True)
    tow_hook = Column('tow_hook', String, nullable=True)
    max_load = Column('max_load', String, nullable=True)
    trailer_weight_b_card = Column('trailer_weight_b_card', String, nullable=True)
    fuel_consumption = Column('fuel_consumption', String, nullable=True)
    co2_transmission = Column('co2_transmission', String, nullable=True)
    service_period = Column('service_period', String, nullable=True)
    service_weight = Column('service_weight', String, nullable=True)
    latest_examination = Column('latest_examination', String, nullable=True)
    taxation_yearly = Column('taxation_yearly', String, nullable=True)
    taxation_weight = Column('taxation_weight', String, nullable=True)
    tow_weight = Column('tow_weight', String, nullable=True)
    total_weight = Column('total_weight', String, nullable=True)

    # other info
    removable_VAT = Column('removable_VAT', String, nullable=True)
    seller_type = Column('seller_type', String, nullable=True)
    export_allowed = Column('export_allowed', String, nullable=True)
    new_car_price = Column('new_car_price', String, nullable=True)
    nr_of_keys = Column('nr_of_keys', String, nullable=True)
    import_type = Column('import_type', String, nullable=True)
    
class BidItem(DeclarativeBase) :
    __tablename__ = "kvd_bid"
    
    object_number = Column(Integer, primary_key = True)
    auction_date = Column('auction_date', String, nullable = True)
    bidder = Column('bidder', String, nullable = True)
    highest_bid = Column('highest_bid', String, nullable = True)
