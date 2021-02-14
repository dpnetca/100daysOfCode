# NOTES:
# I refactored FlightData init after looking at solution, my original
# solution was to take int the full flight API respone and parse it in
# init instead of parsing it fist, and just just passing in interesting
# variables


class FlightData:
    def __init__(
        self,
        departure_city,
        departure_airport,
        destination_city,
        destination_airport,
        departure_date,
        return_date,
        price,
        stop_overs=0,
        via_city="",
    ):

        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.price = price
        self.stop_overs = stop_overs
        self.via_city = via_city
