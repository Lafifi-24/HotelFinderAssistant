import os
import time

import pytest
from datetime import date,timedelta

from Application.navigator import Navigator, BookingApiClient
from Application.hotel import Hotel



        
class TestNavigatorClass:
    
    @pytest.fixture(autouse=True)
    def build_instance(self):
        TestNavigatorClass.navigator = Navigator(BookingApiClient(api_token=os.getenv('BOOKING_API_key')))
    
    @pytest.mark.parametrize("input,expected", [("Marrakech", ('-38833',"Marrakech")),("sdhgh", ('0',"None"))])
    def test_get_city_code(self, input, expected):
        time.sleep(1)
        city_id, city_name = TestNavigatorClass.navigator.get_city_code(input)
        assert city_id == expected[0]
        assert city_name ==  expected[1]
        
    def test_get_hotel_url(self):
        
        time.sleep(1)
        url = TestNavigatorClass.navigator.get_hotel_url('185602', str(date.today() + timedelta(days=1)), str(date.today() + timedelta(days=3)), 'MAD')
        assert isinstance(url, str)
        assert url.startswith('https://www.booking.com/hotel')
        
    def test_get_hotels(self):
        time.sleep(1)
        params ={
            'order_by': 'popularity',
            'adults_number': '2',
            'checkin_date': str(date.today() + timedelta(days=1)),
            'currency': 'MAD',
            'city': 'Marrakech',
            'locale': 'en-gb',
            'checkout_date': str(date.today() + timedelta(days=3)),
            'units': 'metric',
            'room_number': '1',
            'dest_type': 'city',
            'include_adjacency': 'true',
            'children_number': '2',
            'page_number': '0',
            'children_ages': [5,0],
            'class': [3,4],
            'prince':[0,10000]
        }
        hotels = TestNavigatorClass.navigator.get_hotels(params)
        assert isinstance(hotels, list)
        assert isinstance(hotels[0], Hotel)
        assert hotels[0].price <= 10000
        
    
    
        
        
    
    


