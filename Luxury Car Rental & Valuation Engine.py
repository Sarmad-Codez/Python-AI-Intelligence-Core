def calculate_rent(car_model, days):
    # Premium pricing logic based on car tier
    car_model = car_model.lower()
    if "m5" in car_model or "bmw" in car_model:
        rate_per_day = 45000  # Premium Tier
    elif "civic" in car_model:
        rate_per_day = 15000  # Executive Tier
    else:
        rate_per_day = 8000   # Standard Tier

    total_cost = rate_per_day * days
    return total_cost

# Mock testing the engine
car = "BMW M5"
days_requested = 3
print(f"🏎️ Vehicle: {car}")
print(f"💰 Total Rent for {days_requested} days: PKR {calculate_rent(car, days_requested):,}")