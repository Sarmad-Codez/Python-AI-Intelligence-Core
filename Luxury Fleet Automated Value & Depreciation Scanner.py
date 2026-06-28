# Real-time asset inventory tracker (Prices in Lacs)
showroom_inventory = [
    {"car": "Civic Reborn", "base_price": 25, "category": "Standard"},
    {"car": "Honda Civic RS", "base_price": 95, "category": "Sports"},
    {"car": "BMW M5", "base_price": 450, "category": "Elite Luxury"},
    {"car": "Land Cruiser LC300", "base_price": 1200, "category": "Elite Luxury"}
]

print("====================================================")
print("📈 LIVE AUTOMOTIVE PORTFOLIO & MARKET EVALUATOR")
print("====================================================\n")

total_portfolio_value = 0
luxury_units_count = 0

# Iterating through data to compute complex calculations
for item in showroom_inventory:
    print(f"Analyzing Market Metrics for: {item['car']}")
    print(f" -> Category: {item['category']} | Base Evaluation: {item['base_price']} Lacs")
    
    # Process tax and valuation dynamics using conditions
    if item['base_price'] >= 100:
        luxury_units_count += 1
        estimated_tax = item['base_price'] * 0.35  # 35% Luxury Tax
        final_price = item['base_price'] + estimated_tax
        print(f" -> Status: VIP Asset | Luxury Tax Applied: {estimated_tax:.1f} Lacs")
        print(f" -> Final Registration Cost: {final_price:.1f} Lacs")
    else:
        estimated_tax = item['base_price'] * 0.15  # 15% Standard Tax
        final_price = item['base_price'] + estimated_tax
        print(f" -> Status: Standard Asset | Local Tax Applied: {estimated_tax:.1f} Lacs")
        print(f" -> Final Registration Cost: {final_price:.1f} Lacs")
        
    total_portfolio_value += final_price
    print("-" * 45)

print("\n================ FINAL REPORT ================")
print(f"Total Fleet Assets Scanned: {len(showroom_inventory)}")
print(f"High-Value Elite Units Detected: {luxury_units_count}")
print(f"Total Cumulative Portfolio Net Worth: {total_portfolio_value:.2f} Lacs")
print("==============================================")