import sys

class Room:
    """Stores information about a single room."""
    def __init__(self, room_number, rent, persons):
        self.room_number = room_number
        self.rent = rent
        self.persons = persons

class House:
    """Stores all the rooms in the building."""
    def __init__(self):
        self.rooms = []

    def add_room(self, new_room):
        """Adds a room into our house list."""
        self.rooms.append(new_room)

class ExpenseManager:
    """Manages the logic and calculations for the house."""
    def __init__(self):
        self.house = House()

    def process_new_room(self, room_number, rent, persons):
        """Creates a Room object and adds it to the house."""
        room = Room(room_number, rent, persons)
        self.house.add_room(room)

    def calculate_room_rents(self):
        """Calculates the rent per person for each room."""
        results = []
        for room in self.house.rooms:
            if room.persons > 0:
                rent_per_person = room.rent / room.persons
            else:
                rent_per_person = 0.0
            results.append((room.room_number, rent_per_person))
        return results

class CLIController:
    """Handles everything printed to the console and user inputs."""
    def __init__(self):
        self.manager = ExpenseManager()

    def start(self):
        """Runs the main demo output loop."""
        print("Welcome!\n")
        
        while True:
            try:
                num_rooms_text = input("Enter the number of room of your house?\n")
                num_rooms = int(num_rooms_text)
                break
            except ValueError:
                print("Please enter a valid number.")
        
        for i in range(1, num_rooms + 1):
            
            while True:
                try:
                    rent_text = input(f"Enter the rent of room {i}\n")
                    rent = float(rent_text)
                    break
                except ValueError:
                    print("Please enter a valid rent number.")
                    
            while True:
                try:
                    persons_text = input(f"Enter the number of persons in room {i}\n")
                    persons = int(persons_text)
                    break
                except ValueError:
                    print("Please enter a valid number of persons.")
            
            self.manager.process_new_room(room_number=i, rent=rent, persons=persons)

        while True:
            try:
                water_bill_text = input("Enter the water bill\n")
                water_bill = float(water_bill_text)
                break
            except ValueError:
                print("Please enter a valid water bill number.")

        # Print the final calculated math
        print("\n--- Seat Rent Calculations ---")
        rent_results = self.manager.calculate_room_rents()
        for room_no, rent_per_person in rent_results:
            print(f"Room {room_no} per-head rent: {rent_per_person:.2f}")

if __name__ == "__main__":
    controller = CLIController()
    controller.start()
