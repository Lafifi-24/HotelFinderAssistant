

class Hotel:
    def __init__(self, hotel_info:dict):
        self.id = hotel_info['id']
        self.name = hotel_info['name']
        self.photoUrl = hotel_info['photoMainUrl']
        self.propertyClass = hotel_info['propertyClass']
        self.price = hotel_info['priceBreakdown']['grossPrice']['value']
        self.currency = hotel_info['priceBreakdown']['grossPrice']['currency']
        self.reviewScore = hotel_info['reviewScore']
        self.reviewCount = hotel_info['reviewCount']