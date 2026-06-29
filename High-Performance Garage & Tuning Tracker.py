class Supercar:
    def __init__(self, model_name, custom_plate, horsepower):
        self.model_name = model_name
        self.custom_plate = custom_plate
        self.horsepower = horsepower
        self.is_tuned = False

    def apply_stage_1_tuning(self):
        self.horsepower += 50  # Tuning boosts horsepower
        self.is_tuned = True
        print(f"⚡ Stage 1 Tuned! Horsepower increased to {self.horsepower} HP.")

    def display_garage_card(self):
        print("-" * 40)
        print(f"🏎️  Vehicle: {self.model_name}")
        print(f"🔢 Plate: {self.custom_plate}")
        print(f"🔥 Power: {self.horsepower} HP")
        print(f"🏁 Status: {'Ready for Track 🦅' if self.is_tuned else 'Stock Vibe'}")
        print("-" * 40)

# Testing the Python garage system
if __name__ == "__main__":
    # Creating a garage entry
    my_ride = Supercar("Honda Civic RS", "SARMAD", 180)
    my_ride.display_garage_card()

    # Applying tuning logic
    print("\nSending car to the tuning bay...")
    my_ride.apply_stage_1_tuning()
    my_ride.display_garage_card()