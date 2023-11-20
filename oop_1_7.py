class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Mehmon: {self.name}, Yosh: {self.age}")

class Hotel:
    def __init__(self, name):
        self.name = name
        self.guests = []

    def check_in(self, guest):
        self.guests.append(guest)
        print(f"{guest.name} {self.name} mehmonxonasiga kirdi.")

    def check_out(self, guest):
        self.guests.remove(guest)
        print(f"{guest.name} {self.name} mehmonxonasidan chiqdi.")

    def display_guests(self):
        print(f"{self.name} mehmonxonasida joylashgan mehmonlar:")
        for guest in self.guests:
            guest.display_info()

# Test qismi
guest1 = Guest("John", 30)
guest2 = Guest("Martin", 25)

hotel = Hotel("Royal")
hotel.check_in(guest1)
hotel.check_in(guest2)
hotel.display_guests()

hotel.check_out(guest1)
hotel.display_guests()


if __name__ == '__main__':
    pass