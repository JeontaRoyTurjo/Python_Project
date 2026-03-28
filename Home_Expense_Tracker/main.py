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

    def get_total_persons(self):
        """Returns the total number of persons in the house."""
        return sum(room.persons for room in self.house.rooms)

    def calculate_room_rents(self, total_variable_costs=0.0):
        """Calculates the rent per person for each room + shared costs."""
    def get_total_persons(self):
        """Returns the total number of persons in the house."""
        return sum(room.persons for room in self.house.rooms)

    def calculate_room_rents(self, total_variable_costs=0.0):
        """Calculates the rent per person for each room + shared costs."""
        results = []
        total_persons = self.get_total_persons()
        shared_cost_per_head = 0.0
        
        if total_persons > 0:
            shared_cost_per_head = total_variable_costs / total_persons

        total_persons = self.get_total_persons()
        shared_cost_per_head = 0.0
        
        if total_persons > 0:
            shared_cost_per_head = total_variable_costs / total_persons

        for room in self.house.rooms:
            if room.persons > 0:
                rent_per_person = room.rent / room.persons
            else:
                rent_per_person = 0.0
            
            total_per_head = rent_per_person + shared_cost_per_head
            results.append((room.room_number, rent_per_person, total_per_head))
            
        return results, shared_cost_per_head
            
            total_per_head = rent_per_person + shared_cost_per_head
            results.append((room.room_number, rent_per_person, total_per_head))
            
        return results, shared_cost_per_head

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

        while True:
            try:
                wifi_bill = float(input("Enter the Wi-Fi bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")
                
        while True:
            try:
                bua_bill = float(input("Enter the Bua bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                waste_bill = float(input("Enter the waste bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.") 

        while True:
            try:
                electricity_bill = float(input("Enter the electricity bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                gas_bill = float(input("Enter the gas bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                lift_bill = float(input("Enter the lift bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                utility_bill = float(input("Enter the utility bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                water_bill = float(input("Enter the water bill:\n"))
                break
            except ValueError:
                print("Please enter a valid number.")

        # Print the final calculated math
        print("\n--- Seat Rent Calculations ---")
        
        total_variable_costs = water_bill
        
        rent_results, shared_cost_per_head = self.manager.calculate_room_rents(total_variable_costs=total_variable_costs)
        
        if total_variable_costs > 0:
            print(f"Total Shared Variable Costs: {total_variable_costs:.2f}")
            print(f"Variable Costs Per-Head: {shared_cost_per_head:.2f}\n")
            
        for room_no, rent_per_person, total_per_head in rent_results:
            print(f"Room {room_no} -> Base rent per-head: {rent_per_person:.2f} | Total to pay (with bills): {total_per_head:.2f}")
        
        total_variable_costs = wifi_bill + bua_bill + waste_bill + electricity_bill + gas_bill + lift_bill + utility_bill + water_bill
        
        rent_results, shared_cost_per_head = self.manager.calculate_room_rents(total_variable_costs=total_variable_costs)
        
        if total_variable_costs > 0:
            print(f"Total Shared Bills: {total_variable_costs:.2f}")
            print(f"Total bill except rent per-head: {shared_cost_per_head:.2f}\n")
            
        for room_no, rent_per_person, total_per_head in rent_results:
            print(f"Room {room_no} -> Base rent per-head: {rent_per_person:.2f} | Total to pay (with bills): {total_per_head:.2f}")

if __name__ == "__main__":
    controller = CLIController()
    controller.start()
