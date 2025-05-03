# 🔓 Phantom Password Cracking Tool

**Phantom** is an educational and ethical password cracking tool that supports both **brute-force** and **dictionary attacks**. It's built for cybersecurity students, red teamers, and penetration testers to understand password vulnerabilities and hash security mechanisms.

> ⚠️ This tool is intended **for educational purposes only**. Unauthorized use against systems you do not own or have permission to test is illegal.

---

## ⚙️ Features

- 🔐 Supports multiple hashing algorithms: `MD5`, `SHA1`, `SHA256`, `bcrypt`
- 🧠 Brute Force attack using multithreading (ThreadPoolExecutor)
- 📚 Dictionary attack with auto-download from [SecLists](https://github.com/danielmiessler/SecLists)
- 🌐 Async wordlist scraping & downloading via `aiohttp`
- 🧩 Social media hash simulation (Instagram, Facebook, Twitter, LinkedIn)
- ⚡ Simple, clean CLI interface with Phantom branding

---

## 🛠️ Requirements

- Python 3.7+
- `aiohttp` for async HTTP
- `bcrypt` (only if you want to test bcrypt hashes)

Install dependencies:

```bash
pip install aiohttp bcrypt
🚀 Usage
Run the tool:

bash
Copy
Edit
python phantom.py
You will be presented with:

markdown
Copy
Edit
=== Phantom Password Cracking Tool ===
This tool is for educational and ethical testing purposes.

1. Brute Force Attack
2. Dictionary Attack
3. Target Social Media Account
4. Exit
Example: Dictionary Attack
Choose 2 for Dictionary Attack

Enter the hash

Select a wordlist to download (from rockyou variants)

Choose hashing algorithm

Watch it go!

🔐 Supported Hashing Algorithms
Algorithm	Use Case
md5	Legacy systems, older social media (e.g., Facebook)
sha1	Older corporate systems, e.g., LinkedIn dumps
sha256	More secure platforms, e.g., Twitter
bcrypt	Modern systems (expensive hash, slower cracking)

📁 Wordlists
Phantom uses curated wordlists from the SecLists project by default.

🧪 Disclaimer
Phantom is developed for legal penetration testing, educational purposes, and cybersecurity research. Do not use it on systems you do not own or have explicit authorization to test.

💣 Misuse of Phantom may lead to criminal charges. The developers are not responsible for illegal use.

📜 License
MIT License. See LICENSE for details.

👻 Phantom: Ghosting Weak Passwords Since 2025
