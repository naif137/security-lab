import os
import subprocess
from datetime import datetime

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Security Lab Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 20px; }}
        .container {{ max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        .timestamp {{ color: #7f8c8d; font-size: 0.9em; margin-bottom: 20px; }}
        .section {{ margin-top: 25px; }}
        h2 {{ color: #3498db; font-size: 1.2em; }}
        pre {{ background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 5px; overflow-x: auto; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ Security Lab - Automated Report</h1>
        <div class="timestamp">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        
        <div class="section">
            <h2>1. Logged-in Users & System Status</h2>
            <pre>{subprocess.check_output(['w']).decode('utf-8')}</pre>
        </div>

        <div class="section">
            <h2>2. Active Network Ports & Connections</h2>
            <pre>{subprocess.check_output(['ss', '-tuln']).decode('utf-8')}</pre>
        </div>
    </div>
</body>
</html>
"""

with open("security_report.html", "w") as f:
    f.write(html_content)

print("[+] Security HTML Report generated successfully as 'security_report.html'!")

