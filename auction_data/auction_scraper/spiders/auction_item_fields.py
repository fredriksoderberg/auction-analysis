auction_item_fields = {
        'object_number': '//input[@name="item_id"]/@value',
        'auction_URL': '//input[@name="item_url"]/@value',
        'car_model': '//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/h1/text()',
        'description' : '//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/p/text()',
        'place_of_sale' : '//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/ul[2]/li[6]/a/text()',
        'estimated_auction_price': '//*[@id="main"]/div/div[3]/div/div[2]/div[3]/div[1]/ul/li/div/ul[1]/li[2]/div/text()',
        'estimated_dealership_price': '//*[@id="main"]/div/div[3]/div/div[2]/div[3]/div[1]/ul/li/div/ul[1]/li[4]/div/text()',
        'buyer_fee': '//*[@id="main"]/div/div[3]/div/div[2]/div[3]/div[1]/ul/li/div/ul[2]/li[2]/text()',
        'auction_start': '//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/ul[1]/li[2]/p/text()',
        'examiner_comment' : '//div[@id="tab-1"]/div[2]/div[1]/div/ul/p/text()',
        'equipment' : '//div[@id="tab-1"]/div[2]/div[2]/div/ul/p//text()',
        'registration_number' : '//li[text() = "Registreringsnummer"]/following-sibling::li[1]/text()',
        'model_year' : '//li[contains(text(),"Modell")]/following-sibling::li[1]/text()',
        'milage' : '//div[@id="tab-1"]/div[2]/div[3]/ul/li[contains(text(), "llning")]/following-sibling::li[1]/text()',
        'manufactured_date' : '//li[text() = "Tillverkad"]/following-sibling::li[1]/text()',
        'first_time_in_traffic' :'//li[contains(text(), "datum i trafik")]/following-sibling::li[1]/text()',
        'service_book' : '//li[text() = "Servicebok"]/following-sibling::li[1]/text()',
        'transmission' : '//div[@id="tab-1"]/div[2]/div[3]/ul/li[contains(text(), "xell")]/following-sibling::li[1]/text()',
        'nr_of_seats' :'//li[text() = "Antal sittplatser"]/following-sibling::li[1]/text()',
        'color' :'//li[contains(text(), "rg")]/following-sibling::li[1]/text()',
        'car_paint' : '//li[text() = "Lack"]/following-sibling::li[1]/text()',
        'fabric' :  '//*[@id="tab-1"]/div[2]/div[3]/ul/li[22]/text()',
        'new_car_warranty' :'//li[text() = "Nybilsgaranti"]/following-sibling::li[1]/text()',
        'car_damage_warranty' : '//li[text() = "Vagnskadegaranti"]/following-sibling::li[1]/text()',
        'condition_technical_major_notes' : '//div[@id="tab-1"]/div[2]/div[4]/ul/li[contains(text(), "sentliga anm")]/following-sibling::li[1]/text()',
        'condition_technical_other_notes' : '//div[@id="tab-1"]/div[2]/div[4]/ul/li[contains(text(), "vriga anm")]/following-sibling::li[1]/text()',
        'condition_technical_engine' : '//li[text() = "Motor"]/following-sibling::li[1]/text()',
        'condition_technical_transmission': '//div[@id="tab-1"]/div[2]/div[4]/ul/li[contains(text(), "xell")]/following-sibling::li[1]/text()',
        'condition_technical_brakes': '//li[text() = "Bromsar"]/following-sibling::li[1]/text()',
        'condition_technical_service_history' : '//li[text() = "Servicehistorik"]/following-sibling::li[1]/text()',
        'misc_condition_major_notes' : '//div[@id="tab-1"]/div[2]/div[5]/ul/li[contains(text(), "sentliga anm")]/following-sibling::li[1]/text()',
        'misc_condition__other_notes' : '//div[@id="tab-1"]/div[2]/div[5]/ul/li[contains(text(), "vriga anm")]/following-sibling::li[1]/text()',
        'misc_condition_body': '//li[text() = "Kaross"]/following-sibling::li[1]/text()',
        'misc_condition_interior' : '//li[text() = "Inredning"]/following-sibling::li[1]/text()',
        'tyres_current_type' : '//div[@id="tab-1"]/div[2]/div[6]/ul/li[2]/text()',
        'rims_current_type' : '//div[@id="tab-1"]/div[2]/div[6]/ul/li[4]/text()',
        'tyres_current_condtion_front' : '//div[@id="tab-1"]/div[2]/div[6]/ul/li[6]/text()',
        'tyres_current_condtion_back' :'//div[@id="tab-1"]/div[2]/div[6]/ul/li[8]/text()',
        'tyres_extra_type' : '//div[@id="tab-1"]/div[2]/div[6]/ul/li[10]/text()',
        'rims_extra_type' :'//div[@id="tab-1"]/div[2]/div[6]/ul/li[12]/text()',
        'tyres_extra_condtion_front' : '//div[@id="tab-1"]/div[2]/div[6]/ul/li[14]/text()',
        'tyres_extra_condtion_back' : '//div[@id="tab-1"]/div[2]/div[6]/ul/li[16]/text()',
        'chassi_number' : '//li[text() = "Chassienummer"]/following-sibling::li[1]/text()',
        'first_registration' : '//li[contains(text(), "rsta registreringsdatum")]/following-sibling::li[1]/text()',
        'vehicle_year' :'//li[contains(text(), "Fordons")]/following-sibling::li[1]/text()',
        'nr_of_passengers' :'//li[text() = "Passagerare"]/following-sibling::li[1]/text()',
        'engine_effect_kw' : '//li[text() = "Motoreffekt KW"]/following-sibling::li[1]/text()',
        'engine_effect_hp' : '//li[text() = "Motoreffekt HK"]/following-sibling::li[1]/text()',
        'fuel_type' : '//li[text() = "Drivmedel"]/following-sibling::li[1]/text()',
        'tow_hook' : '//li[text() = "Dragkrok"]/following-sibling::li[1]/text()',
        'max_load' : '//li[text() = "Maxlastvikt"]/following-sibling::li[1]/text()',
        'trailer_weight_b_card' : '//li[contains(text(), "pvikt B-k")]/following-sibling::li[1]/text()',
        'fuel_consumption' :'//li[contains(text(), "rbrukning")]/following-sibling::li[1]/text()',
        'co2_transmission' : '//li[contains(text(), "CO2-utsl")]/following-sibling::li[1]/text()',
        'service_period' :  '//li[text() = "Besiktningsperiod"]/following-sibling::li[1]/text()',
        'service_weight' :'//li[contains(text(), "nstevikt")]/following-sibling::li[1]/text()',
        'latest_examination' : '//li[contains(text(), "Senast godk")]/following-sibling::li[1]/text()',
        'taxation_yearly' : '//li[contains(text(), "rsavgift")]/following-sibling::li[1]/text()',
        'taxation_weight' : '//li[text() = "Skattevikt"]/following-sibling::li[1]/text()',
        'tow_weight' : '//div[@id="tab-1"]/div[2]/div[7]/ul/li[not(contains(text(), "pvikt B-k")) and contains(text(), "pvikt")]/following-sibling::li[1]/text()',
        'total_weight' : '//li[text() = "Totalvikt"]/following-sibling::li[1]/text()',
        'removable_VAT' : '//li[text() = "Avlyftbar moms"]/following-sibling::li[1]/text()',
        'seller_type' :'//li[contains(text(), "uppdrag av")]/following-sibling::li[1]/text()',
        'export_allowed' : '//li[text() = "Kan exporteras"]/following-sibling::li[1]/text()',
        'new_car_price' : '//li[contains(text(), "Nypris i grundutf")]/following-sibling::li[1]/text()',
        'nr_of_keys' : '//li[contains(text(), "ljande nycklar")]/following-sibling::li[1]/text()',
        'import_type' : '//li[contains(text(), "Direktimport / Svensks")]/following-sibling::li[1]/text()',
}