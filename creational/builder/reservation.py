import json
from datetime import datetime
from abc import ABC, abstractmethod


class Reservation:
    def __init__(self, arrival_date, departure_date):
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        # self.booking_id = booking_id
        # self.guest = guest
        # self.num_rooms = num_rooms
        # Calculate number of nights as an instance variable
        self.nights = (self.departure_date - self.arrival_date).days

    # Method to convert the object into a dictionary
    def to_dict(self):
        return {
            "arrival_date": self.arrival_date.strftime("%Y-%m-%d"),
            "departure_date": self.departure_date.strftime("%Y-%m-%d"),
            "nights": self.nights
        }

    def __str__(self):
        return f"Arrival: {self.arrival_date}, departure: {self.departure_date}, #nights: {self.nights}"


class Builder(ABC):
    @abstractmethod
    def build(self) -> Reservation:
        pass


# Builder interface
class ReservationBuilder(Builder, ABC):
    def set_arrival_date(self, arrival_date: datetime):
        pass

    def set_departure_date(self, departure_date: datetime):
        self.departure_date = departure_date


# Concrete builder
class BookingReservationBuilder(ReservationBuilder):

    def set_arrival_date(self, arrival_date: datetime):
        self.arrival_date = arrival_date

    def build(self) -> Reservation:
        return Reservation(self.arrival_date, self.departure_date)


if __name__ == "__main__":
    builder = BookingReservationBuilder()
    builder.set_arrival_date(datetime(2021, 12, 15))
    builder.set_departure_date(datetime(2021, 12, 18))

    reservation = builder.build()
    print(reservation)
    print(reservation.arrival_date)
    print(reservation.nights)

    # convert the class object to a dictionary using vars()
    data = reservation.to_dict()
    print(json.dumps(data, indent=4))
