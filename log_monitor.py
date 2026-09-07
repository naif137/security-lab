import os

print("=== Simple Linux Log Monitor ===")
log_path = "/var/log/auth.log"

if os.path.exists(log_path):
    print(f"[+] Scanning {log_path} for failed login attempts...")
    with open(log_path, "r") as f:
        lines = f.readlines()
        failed_attempts = [line for line in lines if "Failed password" in line]
        for attempt in failed_attempts[-5:]: # آخر 5 محاولات فاشلة
            print(attempt.strip())
else:
    print("[-] Auth log file not found or path differs on this WSL distribution.")

