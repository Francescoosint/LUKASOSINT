import os
import time
import requests
from bs4 import BeautifulSoup


def logo():
    os.system("clear" if os.name == "posix" else "cls")
    print(r"""
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \o_)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
      LUKAS OSINT TOOL
 TELEGRAM CHANNEL: @LUKASTOOL
═════════════════════════════
    """)


SOCIAL_MEDIA = {
    "VK": "https://vk.com/{}",
    "Telegram": "https://t.me/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "GitHub": "https://github.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Tumblr": "https://{}.tumblr.com",
    "SoundCloud": "https://soundcloud.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "AskFM": "https://ask.fm/{}",
    "Medium": "https://medium.com/@{}"
}


def get_additional_info(platform, url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            if platform == "VK":
                city = soup.find("a", {"class": "labeled"}).text if soup.find("a", {"class": "labeled"}) else "No additional data available"
                return f"🏙 City: {city}"
            elif platform == "GitHub":
                bio = soup.find("div", {"class": "user-profile-bio"}).text.strip() if soup.find("div", {"class": "user-profile-bio"}) else "No additional data available"
                return f"ℹ Bio: {bio}"
            elif platform == "Facebook":
                work = soup.find("div", {"id": "work"}).text.strip() if soup.find("div", {"id": "work"}) else "No additional data available"
                return f"💼 Work: {work}"
            elif platform == "Instagram":
                bio = soup.find("meta", {"name": "description"})["content"] if soup.find("meta", {"name": "description"}) else "No additional data available"
                return f"📜 Bio: {bio}"
        return "No additional data available"
    except Exception:
        return "No additional data available"


def search_username(username):
    print("\n🔍 Searching...\n")
    found_profiles = []
    additional_info = []

    for platform, url in SOCIAL_MEDIA.items():
        try:
            full_url = url.format(username)
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                found_profiles.append(f"✅ {platform}: {full_url}")
                extra_info = get_additional_info(platform, full_url)
                if extra_info != "No additional data available":
                    additional_info.append(extra_info)
            else:
                found_profiles.append(f"⚠ {platform}: Not Found")
        except requests.exceptions.RequestException:
            found_profiles.append(f"⚠ {platform}: Connection error")

    
    for profile in found_profiles:
        print(profile)

    
    if additional_info:
        print("\n📜 Additional Information:")
        for info in additional_info:
            print(info)
    else:
        print("\n📜 Additional Information: No additional data available")


def main_menu():
    while True:
        logo()
        print("[1] 🔍 Search username")
        print("[2] ❌ Exit")
        print("═════════════════════════════")
        option = input("Select an option: ")

        if option == "1":
            username = input("\nEnter username: ")
            search_username(username)
            input("\nPress Enter to continue...")

        elif option == "2":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n⚠ Invalid option. Try again.")
            time.sleep(2)

# Запуск программы
if __name__ == "__main__":
    main_menu()
