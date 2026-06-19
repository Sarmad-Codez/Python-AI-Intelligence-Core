import random
import string
import os

def encrypt_text(text, shift=4):
    """Simple Caesar Cipher encryption to secure stored passwords"""
    encrypted = ""
    for char in text:
        if char.isalnum():
            encrypted += chr(ord(char) + shift)
        else:
            encrypted += char
    return encrypted

def generate_strong_password(length=12):
    """Generates a highly secure random password"""
    if length < 8:
        length = 8
        
    all_chars = (
        string.ascii_lowercase + 
        string.ascii_uppercase + 
        string.digits + 
        string.punctuation
    )
    
    # Ensure password has at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the length randomly
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    
    return "".join(password)

def save_password(site, username, password):
    """Encrypts and stores credentials into a local file"""
    encrypted_pass = encrypt_text(password)
    with open("vault.txt", "a") as f:
        f.write(f"Website: {site} | Username: {username} | Pass: {encrypted_pass}\n")
    print(f"\n✅ Credentials for {site} secured and saved successfully!")

def view_vault():
    """Displays stored credentials (simulation of file structure)"""
    if not os.path.exists("vault.txt"):
        print("\n📭 Your vault is currently empty.")
        return
        
    print("\n" + "="*50)
    print("            STORED ENCRYPTED VAULT            ")
    print("="*50)
    with open("vault.txt", "r") as f:
        for line in f:
            print(line.strip())
    print("="*50)

def main():
    while True:
        print("\n" + "="*40)
        print("         SECURE PASSWORD VAULT          ")
        print("="*40)
        print("1. Generate & Save a New Password")
        print("2. View Encrypted Vault File Data")
        print("3. Exit")
        print("="*40)
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            site = input("Enter website/app name (e.g. LinkedIn): ").strip()
            username = input("Enter username/email: ").strip()
            
            try:
                length = int(input("Enter password length (Min 8, Default 12): ") or 12)
            except ValueError:
                length = 12
                
            generated_pass = generate_strong_password(length)
            print(f"\n🔑 Generated Password: {generated_pass}")
            
            confirm = input("Do you want to save this password? (y/n): ").strip().lower()
            if confirm == 'y':
                save_password(site, username, generated_pass)
                
        elif choice == '2':
            view_vault()
        elif choice == '3':
            print("\nExiting Password Vault safely. Allah Hafiz! 🔐")
            break
        else:
            print("❌ Invalid option! Try again.")

if __name__ == "__main__":
    main()