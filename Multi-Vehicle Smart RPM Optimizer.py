import time

# Vehicle telemetry dataset
garage_fleet = [
    {"model": "Honda Civic RS", "max_rpm": 7000, "idle_rpm": 900},
    {"model": "BMW M5 Competition", "max_rpm": 7200, "idle_rpm": 800},
    {"model": "Toyota Land Cruiser LC300", "max_rpm": 4500, "idle_rpm": 650}
]

print("====================================================")
print("💻 ENGINEER SARMAD ALI: AUTOMOTIVE AI TELEMETRY CORE")
print("====================================================\n")

for vehicle in garage_fleet:
    print(f"📡 Initializing diagnostics for: {vehicle['model']}")
    print(f"-> Baseline Idle: {vehicle['idle_rpm']} RPM | Max Peak: {vehicle['max_rpm']} RPM")
    
    # Simulate dynamic acceleration loop
    current_rpm = vehicle['idle_rpm']
    step = int((vehicle['max_rpm'] - vehicle['idle_rpm']) / 4)
    
    while current_rpm <= vehicle['max_rpm']:
        print(f"   [RUNNING] Current Engine Speed: {current_rpm} RPM")
        
        # Check safety limits within iteration
        if current_rpm >= (vehicle['max_rpm'] - 1000):
            print("   ⚠️ [ALERT] Approaching Redline! Core temperature rising.")
        else:
            print("   ✅ [OK] Thermal efficiency within nominal range.")
            
        current_rpm += step
        time.sleep(0.4)
        
    print(f"🏁 System Check for {vehicle['model']} COMPLETED.\n")
    print("-" * 50)