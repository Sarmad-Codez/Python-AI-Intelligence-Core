# Bid aur vehicle data variables
print("--- Live Automotive Auction Terminal ---")
car_model = "Toyota Land Cruiser LC300"
reserve_price = 950  # Price in Lacs

print("Current Vehicle on Track:", car_model)
print("Minimum Reserve Price: ", reserve_price, "Lacs")

user_bid = int(input("Apni bidding price enter krein (Lacs mein): "))

# Evaluation logic
if user_bid >= reserve_price:
    print("\n🔨 SOLD! Congratulations, your bid of", user_bid, "Lacs has been ACCEPTED!")
    print("The beast is ready for delivery. Keep grinding! 🏎️💨")
else:
    difference = reserve_price - user_bid
    print("\n❌ BID REJECTED: Your bid is too low.")
    print("Reserve price meet krny k liy mazeed", difference, "Lacs chahiye.")