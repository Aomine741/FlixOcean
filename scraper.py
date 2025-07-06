import requests, json
from bs4 import BeautifulSoup
import uuid

def shorten(url):
    api = "https://gplinks.in/api"
    params = {
        "api": "YOUR_GPLINKS_API_KEY",
        "url": url
    }
    res = requests.get(api, params=params).json()
    return res["shortenedUrl"]

def scrape():
    url = "https://vegamovies.yoga"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    items = []

    for post in soup.select(".post-box"):
        title = post.select_one("h2").text.strip()
        poster = post.select_one("img")["src"]
        link_480 = shorten("https://sample480.com")
        link_720 = shorten("https://sample720.com")
        link_1080 = shorten("https://sample1080.com")
        items.append({
            "id": str(uuid.uuid4()),
            "title": title,
            "poster": poster,
            "links": {
                "480p": link_480,
                "720p": link_720,
                "1080p": link_1080
            }
        })

    with open("backend/data.json", "w") as f:
        json.dump(items, f, indent=2)
