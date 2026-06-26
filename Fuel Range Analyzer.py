# Performance data fields save karna
car_model = "Civic Reborn "
tank_capacity_liters = 50
fuel_average_km_per_liter = 11.5  # Float value

# Total range calculate karna (Capacity * Average)
total_range_km = tank_capacity_liters * fuel_average_km_per_liter

print("\n--- Automotive Range & Fuel Analyzer ---")
print("Vehicle Profile:", car_model)
print("Fuel Tank Size:", tank_capacity_liters, "Liters")
print("Average Fuel Economy:", fuel_average_km_per_liter, "km/L")
print("Total Range on Full Tank:", total_range_km, "Kilometers")
print("Status: Track ready. Keep pushing the RPM!")