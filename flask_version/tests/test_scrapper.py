import json

import pytest
from bs4 import BeautifulSoup


from flaskserver.scrapper import BookingScrapper
from flaskserver.scrapper import Hotel
from samples import exemple_hotel_div_content, exemple_search_params


class TestHotelClass:
    
    def test_Creation(self):
        hotel = Hotel()
        assert isinstance(hotel, Hotel)
        assert hotel.name == None
        assert hotel.stars == None
        assert hotel.link == None
        assert hotel.price == None
        assert hotel.score == None
        assert hotel.taxes == None
        assert hotel.suggestions == None
        assert hotel.client_order == None
    
    def test_extract_hotel_info(self):
        hotel = Hotel()
        hotel.extract_hotel_info(BeautifulSoup(exemple_hotel_div_content, "html.parser"))
        assert hotel.name == 'The Muse Inn'
        assert hotel.stars == 3
        assert hotel.link != None
        assert hotel.price == 'MAD 5,786'
        assert hotel.score == 9.6
        assert 'taxes' in hotel.taxes
        assert 'Room' in hotel.suggestions
        assert 'nights' in hotel.client_order 
        
class TestBookingScrapperClass:
    
    def test_Creation(self):
        scrapper = BookingScrapper()
        assert isinstance(scrapper, BookingScrapper)
        assert scrapper.booking_url != None
        
        
    @pytest.mark.parametrize("input, expected",[
            (dict(city = 'Casablanca',country = 'Morocco'), 'https://www.booking.com/searchresults.en-gb.html?ss=Casablanca,Morocco'),
            (dict(city = 'Casablanca',country = 'Morocco',checkin='XX',checkout='YY'), 'https://www.booking.com/searchresults.en-gb.html?ss=Casablanca,Morocco&checkin=XX&checkout=YY'),
            (dict(city = 'Casablanca',country = 'Morocco',group_adults=2), 'https://www.booking.com/searchresults.en-gb.html?ss=Casablanca,Morocco&group_adults=2'),
            (dict(city = 'Casablanca',country = 'Morocco',no_rooms=2),  'https://www.booking.com/searchresults.en-gb.html?ss=Casablanca,Morocco&no_rooms=2'),
            (dict(city = 'Casablanca',country = 'Morocco',group_children=2,age=[5,6]),'https://www.booking.com/searchresults.en-gb.html?ss=Casablanca,Morocco&group_children=2&age=5&age=6'),
            ({'city':'Casablanca','country':'Morocco','class':'5'},  'https://www.booking.com/searchresults.en-gb.html?ss=Casablanca,Morocco&nflt=class%3D5'),

        ] )
    def test_build_path(self,input,expected):
        scrapper = BookingScrapper()
        path = scrapper.build_path(input)
        assert path == expected
        
    def test_scrape(self):
        scrapper = BookingScrapper()
        hotels = scrapper.scrape(json.loads(exemple_search_params))
        assert len(hotels) > 0
        assert isinstance(hotels[0],Hotel)
        for hotel in hotels:
            assert hotel.name != None
            assert hotel.stars == 5
            assert hotel.link != None
            assert hotel.price != None
            assert hotel.score != None
            assert 'taxes' in hotel.taxes
            assert 'Room' in hotel.suggestions
            assert 'nights' in hotel.client_order 
        
        
    
    


