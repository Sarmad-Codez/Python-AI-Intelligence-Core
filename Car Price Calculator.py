# User se gaari ki base price aur modifications ki cost input lena
print("--- Professional Car Customizer ---")
base_car_price = int(input("Gaari ki base price enter krein (PKR): "))
alloy_rims_cost = int(input("Custom Alloy Rims ki cost enter krein (PKR): "))
body_kit_cost = int(input("Aesthetic Body Kit ki cost enter krein (PKR): "))

# Total budget calculate karna
total_project_cost = base_car_price + alloy_rims_cost + body_kit_cost

print("\n--- Final Customized Car Invoice ---")
print("Base Car Value: PKR", base_car_price)
print("Total Mods Added: PKR", (alloy_rims_cost + body_kit_cost))
print("Net Total Price of the Beast: PKR", total_project_cost)