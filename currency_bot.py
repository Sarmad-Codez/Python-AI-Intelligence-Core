import urllib.request
import json
import time

def get_live_rates():
    # Free reliable public API endpoint for current conversion bases
    api_url = "https://open.er-api.com/v6/latest/PKR"
    
    print("\n[Accessing International Exchange Matrix...]")
    time.sleep(0.4)
    
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        # Rates returned are 1 PKR = X foreign currency
        rates = data.get("rates", {})
        return rates
    except Exception as e:
        print(f"❌ Connection Interrupted: Unable to sync global rates. Error: {e}")
        return None

def main():
    print("="*50)
    print("         LIVE REAL-TIME CURRENCY CONVERTER        ")
    print("="*50)
    
    rates = get_live_rates()
    if not rates:
        print("👉 Make sure your system is online to sync live rates.")
        return
        
    print("✅ Currency conversion rates synchronized successfully!")
    
    try:
        pkr_amount = float(input("\nEnter amount in Pakistani Rupees (PKR): "))
    except ValueError:
        print("❌ Invalid entry! Please type numbers only.")
        return

    # Target conversion mapping (Inverting the base rate since API is base PKR)
    usd_amount = pkr_amount * rates.get("USD", 0)
    gbp_amount = pkr_amount * rates.get("GBP", 0)
    sar_amount = pkr_amount * rates.get("SAR", 0)

    print("\n" + "="*45)
    print(f"💵 Base Amount: {pkr_amount:,.2f} PKR")
    print("="*45)
    print(f"🇺🇸 Equivalent in USD: ${usd_amount:,.2f} USD")
    print(f"🇬🇧 Equivalent in GBP: £{gbp_amount:,.2f} GBP")
    print(f"🇸🇦 Equivalent in SAR: {sar_amount:,.2f} SAR")
    print("="*45)
    print(f"📊 Global Update Timestamp: {data_time := data.get('time_last_update_utc', 'Just Now') if 'data' in locals() else 'Just Now'}")

if __name__ == "__main__":
    main()