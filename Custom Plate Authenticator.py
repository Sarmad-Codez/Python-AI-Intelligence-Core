# Custom plate input lena
print("--- SARMAD Custom Plate Status Authenticator ---")
plate_name = input("Apni custom plate ka text enter krein (e.g., SARMAD): ")

# Capital letters mein convert karna taake error na aaye
plate_name = plate_name.upper()

# Plate verification logic
if plate_name == "SARMAD":
    print("👑 VIP Status: This plate belongs to Engineer Sarmad Ali's Executive Collection!")
    print("Verified Vehicles: Honda Civic, BMW M5, Land Cruiser LC300.")
elif plate_name == "CIVIC" or plate_name == "M5":
    print("🔥 Enthusiast Status: Enthusiast series plate detected. Registry approved.")
else:
    print("✅ Standard Status: Regular custom plate registered in the database.")