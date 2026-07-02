# Luxury SUV Rental Fee Calculator
def calculate_rent(car_choice, days):
    # Rates per day in PKR
    rates = {
        "1": {"name": "Toyota Land Cruiser V8", "rate": 80000},
        "2": {"name": "Lexus LC300", "rate": 120000}
    }
    
    if car_choice not in rates:
        return "Invalid Choice!"
        
    selected_car = rates[car_choice]["name"]
    per_day_cost = rates[car_choice]["rate"]
    
    total_rent = per_day_cost * days
    security_deposit = total_rent * 0.20 # 20% security deposit
    
    return selected_car, total_rent, security_deposit

# Running the app
print("⚡ WELCOME TO LAHORE LUXURY RENTALS ⚡")
print("1. Toyota Land Cruiser V8")
print("2. Lexus LC300")

choice = input("Select your beast (1 or 2): ")
days_to_rent = int(input("Enter number of days for rental: "))

result = calculate_rent(choice, days_to_rent)

if result == "Invalid Choice!":
    print("Jaani, sahi gari select karo!")
else:
    car_name, rent, security = result
    print("\n" + "="*30)
    print(f"🚗 Vehicle: {car_name}")
    print(f"📅 Total Days: {days_to_rent}")
    print(f"💰 Total Rent: {rent:,} PKR")
    print(f"🛡️ Refundable Security (20%): {security:,} PKR")
    print("="*30)# Luxury SUV Rental Fee Calculator
def calculate_rent(car_choice, days):
    # Rates per day in PKR
    rates = {
        "1": {"name": "Toyota Land Cruiser V8", "rate": 80000},
        "2": {"name": "Lexus LC300", "rate": 120000}
    }
    
    if car_choice not in rates:
        return "Invalid Choice!"
        
    selected_car = rates[car_choice]["name"]
    per_day_cost = rates[car_choice]["rate"]
    
    total_rent = per_day_cost * days
    security_deposit = total_rent * 0.20 # 20% security deposit
    
    return selected_car, total_rent, security_deposit

# Running the app
print("⚡ WELCOME TO LAHORE LUXURY RENTALS ⚡")
print("1. Toyota Land Cruiser V8")
print("2. Lexus LC300")

choice = input("Select your beast (1 or 2): ")
days_to_rent = int(input("Enter number of days for rental: "))

result = calculate_rent(choice, days_to_rent)

if result == "Invalid Choice!":
    print("Jaani, sahi gari select karo!")
else:
    car_name, rent, security = result
    print("\n" + "="*30)
    print(f"🚗 Vehicle: {car_name}")
    print(f"📅 Total Days: {days_to_rent}")
    print(f"💰 Total Rent: {rent:,} PKR")
    print(f"🛡️ Refundable Security (20%): {security:,} PKR")
    print("="*30)