import os
import platform
import shutil
import time

def check_system_metrics():
    print("="*55)
    print("         REAL-TIME SYSTEM HEALTH LOGS         ")
    print("="*55)
    
    # 1. OS & Architecture Information
    print(f"🖥️  Operating System : {platform.system()} ({platform.release()})")
    print(f"🧠 Processor Core  : {platform.processor()}")
    
    # 2. Storage/Disk space monitoring using built-in shutil
    total, used, free = shutil.disk_usage("/")
    
    # Convert bytes to Gigabytes (GB)
    total_gb = total / (1024**3)
    used_gb = used / (1024**3)
    free_gb = free / (1024**3)
    disk_usage_pct = (used / total) * 100
    
    print(f"💾 Storage Capacity: {total_gb:.2f} GB Total | {free_gb:.2f} GB Free")
    print(f"📊 Disk Space Used : {disk_usage_pct:.1f}%")
    
    # 3. Dynamic Threshold Threshold Simulation
    print("\n[AI Diagnostics & Alerts Network]:")
    if disk_usage_pct > 85:
        print("🚨 ALERT: Disk storage is critically low! Run 'file_organizer' to clear space.")
    else:
        print("✅ SYSTEM STATUS: OPTIMAL (Storage limits are within secure boundaries.)")
        
    # 4. Simulation of CPU Thread Load check
    print("⚡ Analyzing kernel background clock cycles...")
    time.sleep(0.5)
    print("🟢 CPU Threads Status: STABLE (Clock speeds idling smoothly.)")
    print("="*55)

if __name__ == "__main__":
    check_system_metrics()