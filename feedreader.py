import feedparser

def fetch_feed(url):
    feed = feedparser.parse(url)
    items = []

    for entry in feed.entries:
        items.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary if "summary" in entry else "",
            "published": entry.published if "published" in entry else ""
        })

    return items
