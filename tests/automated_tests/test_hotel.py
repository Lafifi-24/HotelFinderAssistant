from Application.hotel import Hotel

class TestHotelClass:
    
    def test_Creation(self):
        
        example = {
            'id': '123',
            'name': 'testName',
            'photoMainUrl': 'testUrl',
            'propertyClass': 'testClass',
            'priceBreakdown': {
                'grossPrice': {
                    'value': 'testValue',
                    'currency': 'testCurrency'
                }
            },
            'reviewScore': 'testScore',
            'reviewCount': 'testCount'
        }
        hotel = Hotel(example)
        assert isinstance(hotel, Hotel)
        assert hotel.id == example['id']
        assert hotel.name == example['name']
        assert hotel.photoUrl == example['photoMainUrl']
        assert hotel.propertyClass == example['propertyClass']
        assert hotel.price == example['priceBreakdown']['grossPrice']['value']
        assert hotel.currency == example['priceBreakdown']['grossPrice']['currency']
        assert hotel.reviewScore == example['reviewScore']
        assert hotel.reviewCount == example['reviewCount']