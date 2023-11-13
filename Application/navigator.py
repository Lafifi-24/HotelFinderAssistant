import re

import requests

from Application.hotel import Hotel


class BookingApiClient:
    def __init__(self, api_token):
        self.api_token = api_token

    def make_api_request(self, url, params):
        headers = {
            "X-RapidAPI-Key": self.api_token,
            "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=params)

        return response.json()
    
    

class Navigator:
    def __init__(self, booking_api:BookingApiClient):
        self.booking_api = booking_api
        self.cities = {}
        
    def get_city_code(self, city_name):
        url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

        querystring = {"name":city_name,"locale":"en-gb"}

        answer = self.booking_api.make_api_request(url, querystring)
        
        for dictionary in answer:
            if dictionary['dest_type'] == 'city':
                return dictionary['dest_id'], dictionary['name']
        return '0',"None"
    
    def get_hotel_url(self, hotel_id, checkin, checkout, currency):
        
        url = "https://booking-com.p.rapidapi.com/v2/hotels/details"

        querystring = {"hotel_id":hotel_id,"currency":currency,"locale":"en-gb","checkout_date":checkout,"checkin_date":checkin}

        answer = self.booking_api.make_api_request(url, querystring)
    
        
        return answer['url']
    
    def build_url_with_params(self, url, params):
        keys = ['checkin_date', 'checkout_date', 'adults_number', 'children_number','age', 'room_number', 'currency']
        url += '?'
        
        for key in keys:
            if key == 'age':
                for element in params['children_ages']:
                    url += f'&{key}={element}'
            else:
                url += f'&{key}={params[key]}'  
        return url
        
    
    def build_query_params_for_hotels_search(self, params):
        
        querystring = {
            'order_by': params['order_by'],
            'adults_number': str(params['adults_number']),
            'checkin_date': params['checkin_date'],
            'filter_by_currency': params['currency'],
            'dest_id': params['city_id'],
            'locale': 'en-gb',
            'checkout_date': params['checkout_date'],
            'units': 'metric',
            'room_number': params['room_number'],
            'dest_type': 'city',
            'include_adjacency': 'true',
            'page_number': '0',

            'categories_filter_ids': 'free_cancellation::1'}
        
        if 'children_ages' in params:
            if len(params['children_ages']) > 0:
                querystring['children_ages'] =','.join([str(age) for age in params['children_ages']])
        if 'children_number' in params:
            if int(params['children_number']) > 1:
               querystring['children_number'] = params["children_number"]
        
        if 'class' in params:
            for _class in params['class']:
                querystring['categories_filter_ids'] += f',class::{_class}'
        if 'price' in params:
            if len(params['price']) > 1:
                querystring['categories_filter_ids'] += f',price::{params["currency"]}-{params["price"][0]}-{params["price"][1]}'
            
        return querystring
    
    
    def get_hotels(self, params):
        url = "https://booking-com.p.rapidapi.com/v2/hotels/search"
        
        if params['city'] not in self.cities:
            city_id, city_name = self.get_city_code(params['city'])
            if city_id == '0':
                return []
            if city_name != params['city']:
                self.cities[city_name] = city_id # to avoid duplicates for small faults in the city name
            self.cities[params['city']] = city_id
            
        params['city_id'] = self.cities[params['city']]
        
        querystring = self.build_query_params_for_hotels_search(params)
            
        answer= self.booking_api.make_api_request(url, querystring)
        
        hotels = []

        for hotel in answer['results']:
            
            hotels.append(Hotel(hotel))
            
        return hotels

