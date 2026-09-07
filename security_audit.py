import os
import subprocess

print("=== Advanced Linux Security Audit ===")

# فحص مستخدمي النظام النشطين
print("\n[1] Logged-in Users:")
subprocess.run(["w"])

# فحص صلاحيات ملفات الهوية الحساسة
print("\n[2] Checking Sensitive Files Permissions:")
sensitive_files = ["/etc/passwd", "/etc/shadow"]
for f in sensitive_files:
    if os.path.exists(f):
        perms = oct(os.stat(f).st_mode)[-3:]
        print(f"File {f}: Permissions {perms}")

# فحص العمليات المشبوهة أو الجارية
print("\n[3] Top Running Processes:")
subprocess.run(["ps", "aux", "--sort=-%mem"])

