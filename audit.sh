#!/bin/bash
echo "=== System Security Audit ==="
echo "[+] Current User: $(whoami)"
echo "[+] Logged in users:"
who
echo "[+] Disk Usage:"
df -h /
echo "[+] Active Network Connections:"
ss -tuln

