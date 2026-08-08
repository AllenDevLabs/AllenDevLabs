import os
import subprocess
import webbrowser
from pathlib import Path

print("=== Tech Business Setup ===")

name = input("Your name: ")
business = input("Business name: ")
github = input("GitHub username: ")

base = Path.home() / "TechBusiness"

folders = [
    "Portfolio",
    "PC-Repair",
    "Networking",
    "Linux-HomeLab",
    "Windows-Scripts",
    "Smart-TV",
    "Invoices",
    "Marketing"
]

for folder in folders:
    path = base / folder
    path.mkdir(parents=True, exist_ok=True)

print("Folders created!")

readme = f"""
# {business}

Computer and Smart TV Technician

Owner: {name}

## Services

- Computer repair
- Windows installation
- Virus removal
- Smart TV setup
- WiFi troubleshooting
- Home networking

GitHub:
https://github.com/{github}
"""

(base / "README.md").write_text(readme)

portfolio = """
<!DOCTYPE html>
<html>
<head>
<title>Tech Services</title>
</head>

<body>

<h1>Computer & Smart TV Technician</h1>

<h2>Services</h2>

<ul>
<li>PC Repair</li>
<li>Smart TV Setup</li>
<li>Networking</li>
<li>Remote Support</li>
</ul>

</body>
</html>
"""

(base / "Portfolio" / "index.html").write_text(portfolio)

print("Portfolio created!")

print("""
Next steps:

1. Sign into GitHub with your passkey.
2. Run:

gh auth login

3. Create your repositories.
""")

websites = [
    "https://github.com",
    "https://www.fiverr.com",
    "https://www.linkedin.com",
    "https://www.facebook.com/marketplace"
]

open_sites = input("Open business websites? y/n: ")

if open_sites.lower() == "y":
    for site in websites:
        webbrowser.open(site)

print("Setup complete!")
