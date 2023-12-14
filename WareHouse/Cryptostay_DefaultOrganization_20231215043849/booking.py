'''
This file defines the Booking class.
'''
class Booking:
    def __init__(self, user, hotel, check_in, check_out, payment_details):
        self.user = user
        self.hotel = hotel
        self.check_in = check_in
        self.check_out = check_out
        self.payment_details = payment_details