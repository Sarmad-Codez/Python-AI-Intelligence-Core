import urllib.request
import re
import time

def scrape_quotes_data():
    # Target URL: A safe website designed for scrapers to practice
    target_url = "https://quotes.toscrape.com/"
    
    print("\n[Launching Web Data Scraper Subroutine...]")
    print(f"🌐 Connecting to target matrix: {target_url}")
    time.sleep(0.5)
    
    try:
        # Request web content
        req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode('utf-8')
            
        print("📥 HTML data packet successfully received. Parsing structure...")
        time.sleep(0.4)
        
        # Regex to find text inside quotes span tag: <span class="text" itemprop="text">“...”</span>
        quotes = re.findall(r'<span class="text" itemprop="text">“(.*?)”</span>', html_content)
        # Regex to find authors inside small tag: <small class="author" itemprop="author">...</small>
        authors = re.findall(r'<small class="author" itemprop="author">(.*?)</small>', html_content)
        
        print("\n" + "="*50)
        print("          EXTRACTED INTERNET KNOWLEDGE DATA       ")
        print("="*50)
        
        # Open a local text file to store the scraped clean data
        with open("scraped_quotes.txt", "w", encoding="utf-8") as file:
            file.write("=== SCRAPED QUOTES PORTFOLIO ===\n\n")
            
            for i in range(min(len(quotes), 5)):  # Extract top 5 items for clean preview
                clean_quote = quotes[i]
                clean_author = authors[i]
                
                output_line = f"💬 Quote: \"{clean_quote}\"\n👤 Author: {clean_author}\n"
                print(output_line)
                
                # Write inside local repository file
                file.write(output_line + "-"*40 + "\n")
                
        print("="*50)
        print("✅ Data successfully structured and saved inside 'scraped_quotes.txt'!")
        
    except Exception as e:
        print(f"❌ Scraping Failed: {e}")
        print("👉 Check your internet connection or target endpoint access restrictions.")

if __name__ == "__main__":
    scrape_quotes_data()