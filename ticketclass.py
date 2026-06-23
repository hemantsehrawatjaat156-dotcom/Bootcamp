class Ticket:
    def __init__(self, movie, seats_available, seats_required):
        self.movie = movie
        self.seats_available = seats_available
        self.seats_required = seats_required

        self.confirmed_seats = min(seats_available, seats_required)

        if seats_available >= seats_required:
            self.message = "Full request confirmed."
        else:
            self.message = (
                f"Only {self.confirmed_seats} seat(s) confirmed. "
                f"{seats_required - self.confirmed_seats} seat(s) unavailable."
            )

    def display(self):
        print(f"Movie: {self.movie}")
        print(f"Seats Requested: {self.seats_required}")
        print(f"Seats Available: {self.seats_available}")
        print(f"Confirmed Seats: {self.confirmed_seats}")
        print(f"Message: {self.message}")
        print("-" * 40)


ticket1 = Ticket("Avengers: Endgame", 10, 4)  
ticket2 = Ticket("Inception", 3, 5)           
ticket3 = Ticket("Interstellar", 0, 2)        


ticket1.display()
ticket2.display()
ticket3.display()
