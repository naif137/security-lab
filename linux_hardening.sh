#!/bin/bash
echo "=== Linux Hardening & Audit Script ==="
echo "[+] Checking Sudoers file permissions..."
ls -l /etc/sudoers

echo "[+] Checking for users with UID 0 (root privileges):"
awk -F: '($3 == 0) {print $1}' /etc/passwd

echo "[+] Checking critical listening ports..."
ss -tuln | grep LISTEN


