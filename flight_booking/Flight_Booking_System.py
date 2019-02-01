import time


class BookingClass(object):
    business = "BUSINESS"
    economy = "ECONOMY"


class SeatingArea(object):
    def __init__(self, booking_class, start_row, row_count, seats_per_row):
        self.booking_class = booking_class
        self.start_row = start_row
        self.row_count = row_count
        self.seats_per_row = seats_per_row
        self.total_seats = row_count * seats_per_row
        self.window_seats = 2 * self.row_count
        self.Aisle = 2 * self.row_count
        self.otherSeats = self.total_seats - (self.Aisle + self.window_seats)
        self.book_count = 0
        self.remaining_seat_count = 0

    def get_booking_class(self):
        return self.booking_class

    def get_start_row(self):
        return self.start_row

    def get_row_count(self):
        return self.row_count

    def get_seats_per_row(self):
        return self.seats_per_row

    def get_total_seats(self):
        return self.total_seats

    def get_window_seats(self):
        return self.window_seats

    def get_aisle(self):
        return self.Aisle

    def get_middle_seats(self):
        return self.otherSeats

    def get_book_count(self):
        return self.book_count

    def get_remaining_count(self):
        return self.remaining_seat_count


business = SeatingArea(booking_class=BookingClass.business, start_row=1, row_count=5, seats_per_row=6)
economy = SeatingArea(booking_class=BookingClass.economy, start_row=6, row_count=20, seats_per_row=8)
business_seats = business.get_total_seats()
economy_seats = economy.get_total_seats()
business_window_seats = business.get_window_seats()
economy_window_seats = economy.get_window_seats()
business_aisle_seats = business.get_aisle()
economy_aisle_seats = economy.get_aisle()
business_middle_seats = business.get_middle_seats()
economy_middle_seats = economy.get_middle_seats()
business_book_count = business.get_book_count()
business_remaining_seat_count = business.get_remaining_count()
business_total_seats = business.get_total_seats()
economy_book_count = economy.get_book_count()
economy_remaining_seat_count = economy.get_remaining_count()
economy_total_seats = economy.get_total_seats()
book_count = business_book_count + economy_book_count
remaining_seat_count = business_remaining_seat_count + economy_remaining_seat_count
total_seats = business_total_seats + economy_total_seats

while True:

    response = raw_input('Do you want to book a ticket now?    ')

    if response == "yes":

        class_response = raw_input("Which class do you prefer ?")

        if class_response == "business":
            seat_response = raw_input("Which Seat do you want ? window | aisle  :  ")
            if seat_response == "window":
                print "Please wait I am booking window seat for you ..."
                time.sleep(2)
                business_window_seats -= 1
                print "Window seats remaining = {} ".format(business_window_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)

            elif seat_response == "aisle":
                print "Please wait I am booking aisle seat for you ..."
                time.sleep(2)
                business_aisle_seats -= 1
                print "Window seats remaining = {} ".format(business_aisle_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)

            elif seat_response == "middle":
                print "Please wait I am booking middle seat for you ..."
                time.sleep(2)
                business_middle_seats -= 1
                print "Window seats remaining = {} ".format(business_aisle_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)
                print "Window seats remaining = {} ".format(business_aisle_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)
            else:
                print "You made a wrong choice"

        if class_response == "economy":
            seat_response = raw_input("Which Seat do you want ? window | aisle  :  ")
            if seat_response == "window":
                print "Please wait I am booking window seat for you ..."
                time.sleep(2)
                economy_window_seats -= 1
                print "Window seats remaining = {} ".format(economy_window_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)

            elif seat_response == "aisle":
                print "Please wait I am booking aisle seat for you ..."
                time.sleep(2)
                economy_aisle_seats -= 1
                print "Window seats remaining = {} ".format(economy_aisle_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)

            elif seat_response == "middle":
                print "Please wait I am booking middle seat for you ..."
                time.sleep(2)
                print "Please wait I am booking aisle seat for you ..."
                time.sleep(2)
                economy_middle_seats -= 1
                print "Window seats remaining = {} ".format(economy_middle_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)
                print "Window seats remaining = {} ".format(business_aisle_seats)
                book_count += 1
                remaining_seat_count = total_seats - book_count
                print "Total seats booked  = {}".format(book_count)
                print "Total seats remaining = {}".format(remaining_seat_count)

            else:
                print "You made a wrong choice"

    else:
        print "Thanks for using Flight Booking system"
        break



