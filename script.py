import hashlib
import itertools
import threading
import asyncio
import aiohttp
import os
from concurrent.futures import ThreadPoolExecutor

# Phantom branding
BRAND_NAME = "Phantom"

# Function to hash the password (supports multiple algorithms)
def hash_password(password, algorithm="md5"):
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == "bcrypt":
        # For bcrypt, you would need to use a library like `bcrypt` to hash and check passwords
        import bcrypt
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return None

# Brute Force Attack using ThreadPoolExecutor for parallel processing
def brute_force_crack(hash_to_crack, algorithm="md5"):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_length = 5  # Limiting length to 5 for demo

    print(f"Starting brute-force attack with {BRAND_NAME}... (this may take time)")
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for length in range(1, max_length + 1):  # Try lengths 1-5
            for password in itertools.product(chars, repeat=length):
                guess = ''.join(password)
                futures.append(executor.submit(check_hash, guess, hash_to_crack, algorithm))
        
        for future in futures:
            result = future.result()
            if result:
                print(f"Password found: {result}")
                return result
    print("Password not found.")
    return None

# Function to check hash comparison (to be used in ThreadPoolExecutor)
def check_hash(guess, hash_to_crack, algorithm):
    if hash_password(guess, algorithm) == hash_to_crack:
        return guess
    return None

# Asynchronous function to download wordlist using aiohttp (non-blocking, fast)
async def download_wordlist(url, download_path):
    print(f"Downloading wordlist from {url}... ({BRAND_NAME})")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(download_path, 'wb') as file:
                    file.write(await response.read())
                print(f"Wordlist downloaded successfully to {download_path} ({BRAND_NAME})")
            else:
                print(f"Failed to download wordlist from {url} ({BRAND_NAME})")

# Scraping wordlist links from GitHub using direct raw content
async def scrape_wordlists():
    print(f"Scraping wordlist files from SecLists... ({BRAND_NAME})")

    # URL for the SecLists raw wordlist files (GitHub API endpoints)
    SECLISTS_RAW_URLS = [
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-75.txt",
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou.txt"
    ]

    return SECLISTS_RAW_URLS

# Select wordlist to download
def list_and_download_wordlist():
    loop = asyncio.get_event_loop()
    wordlist_links = loop.run_until_complete(scrape_wordlists())
    
    if not wordlist_links:
        print("No wordlist files found.")
        return None
    
    print("\nAvailable Wordlists:")
    for i, link in enumerate(wordlist_links, 1):
        print(f"{i}. {link}")
    
    choice = int(input("\nChoose a wordlist to download (number): ").strip())
    
    if choice < 1 or choice > len(wordlist_links):
        print("Invalid choice.")
        return None
    
    selected_url = wordlist_links[choice - 1]
    download_path = input("Enter the download path (e.g., /path/to/wordlist.txt): ").strip()
    
    # Download selected wordlist
    loop.run_until_complete(download_wordlist(selected_url, download_path))
    
    return download_path

# Dictionary attack optimized with set-based lookup for speed
def dictionary_attack(hash_to_crack, wordlist, algorithm="md5"):
    print(f"Starting dictionary attack using {wordlist}... ({BRAND_NAME})")
    with open(wordlist, "r") as file:
        wordset = set(file.read().splitlines())  # Using set for O(1) lookup time
    print(f"Loaded {len(wordset)} words for dictionary attack.")
    
    for word in wordset:
        if hash_password(word, algorithm) == hash_to_crack:
            print(f"Password found: {word}")
            return word
    print("Password not found.")
    return None

# Function to select social media platform
def select_social_media_platform():
    print(f"\n=== Select Social Media Platform ({BRAND_NAME}) ===")
    print("1. Instagram (MD5 hash)")
    print("2. Facebook (MD5 hash)")
    print("3. Twitter (SHA256 hash)")
    print("4. LinkedIn (SHA1 hash)")
    print("5. Back to Main Menu")
    
    platform_choice = input("\nChoose a platform (1/2/3/4/5): ").strip()
    
    if platform_choice == "1":
        return "Instagram", "md5"
    elif platform_choice == "2":
        return "Facebook", "md5"
    elif platform_choice == "3":
        return "Twitter", "sha256"
    elif platform_choice == "4":
        return "LinkedIn", "sha1"
    elif platform_choice == "5":
        return None, None
    else:
        print("Invalid choice. Please select again.")
        return select_social_media_platform()

# Main menu and logic
def main():
    print(f"\n=== {BRAND_NAME} Password Cracking Tool ===")
    print(f"This tool is for educational and ethical testing purposes. ({BRAND_NAME})")
    print("==========================================\n")

    while True:
        print(f"1. Brute Force Attack ({BRAND_NAME})")
        print(f"2. Dictionary Attack ({BRAND_NAME})")
        print(f"3. Target Social Media Account ({BRAND_NAME})")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ").strip()

        if choice == "1":
            hash_to_crack = input("Enter the hash to crack: ").strip()
            algorithm_choice = input("Choose algorithm (md5, sha256, sha1, bcrypt): ").strip().lower()
            brute_force_crack(hash_to_crack, algorithm_choice)

        elif choice == "2":
            hash_to_crack = input("Enter the hash to crack: ").strip()
            wordlist = list_and_download_wordlist()  # Download wordlist if needed
            if wordlist:
                algorithm_choice = input("Choose algorithm (md5, sha256, sha1, bcrypt): ").strip().lower()
                dictionary_attack(hash_to_crack, wordlist, algorithm_choice)

        elif choice == "3":
            platform, algorithm = select_social_media_platform()
            if platform:
                print(f"Targeting {platform} account with {algorithm} hash algorithm... ({BRAND_NAME})")
                hash_to_crack = input("Enter the hash to crack (social media password hash): ").strip()
                wordlist = list_and_download_wordlist()  # Download wordlist if needed
                if wordlist:
                    dictionary_attack(hash_to_crack, wordlist, algorithm)

        elif choice == "4":
            print(f"Exiting {BRAND_NAME} tool...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the tool
if __name__ == "__main__":
    main()
