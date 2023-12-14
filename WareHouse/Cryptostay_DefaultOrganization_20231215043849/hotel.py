'''
This file defines the Hotel class.
'''
class Hotel:
    def __init__(self, name, location, availability, price):
        self.name = name
        self.location = location
        self.availability = availability
        self.price = price
        self.rooms = []
    def book_room(self, user, check_in, check_out, payment_details):
        if self.check_availability(check_in, check_out):
            booking = Booking(user, self, check_in, check_out, payment_details)
            self.rooms.append(booking)
            user.bookings.append(booking)
            return True
        else:
            return False
    def check_availability(self, check_in, check_out):
        for room in self.rooms:
            if room.check_in <= check_out and room.check_out >= check_in:
                return False
        return True
    def get_info(self):
        return f"Name: {self.name}\nLocation: {self.location}\nAvailability: {self.availability}\nPrice: {self.price}"