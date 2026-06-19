import urllib.request
import json
import time

def fetch_live_crypto_rates():
    # Public API URL to get live prices from CoinGecko
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
    
    print("\n[Connecting to Live Web Server: Fetching Market Feeds...]")
    time.sleep(0.5)
    
    try:
        # Using built-in urllib to make API requests without installing extra packages
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        btc_price = data['bitcoin']['usd']
        eth_price = data['ethereum']['usd']
        sol_price = data['solana']['usd']
        
        print("="*50)
        print("         LIVE CRYPTO MONITORING NETWORK       ")
        print("="*50)
        print(f"🪙 Bitcoin (BTC):  ${btc_price:,} USD")
        print(f"🔷 Ethereum (ETH): ${eth_price:,} USD")
        print(f"☀️ Solana (SOL):   ${sol_price:,} USD")
        print("="*50)
        
        # Simple AI baseline analysis model
        print("\n[AI Market Trend Analysis]:")
        if btc_price > 60000:
            print("➡️ Market Status: BULLISH TREND (BTC holding strong ground above $60k threshold.)")
        else:
            print("➡️ Market Status: CONSOLIDATION (Prices resting inside normal support levels.)")
            
    except Exception as e:
        print(f"❌ Network Error: Unable to fetch live web data. Details: {e}")
        print("👉 Make sure your laptop/PC is connected to the internet!")

if __name__ == "__main__":
    fetch_live_crypto_rates()