from feed_reader import fetch_feed
from ai_processor import summarize_text
from twitter_sender import post_to_twitter
from linkedin_sender import post_to_linkedin

FEEDS = [
    "https://www.wired.com/feed/category/ai/",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://feeds.feedburner.com/venturebeat/ai"
]

def process_feed():
    for feed_url in FEEDS:
        print(f"\n📡 Fetching feed: {feed_url}")
        items = fetch_feed(feed_url)

        for item in items[:3]:  # pick the first 3 from each feed
            summary = summarize_text(item["summary"])

            message = f"{item['title']}\n\n{summary}\n\n{item['link']}"

            post_to_twitter(message)
            post_to_linkedin(message)

            print("Posted:", item["title"])

process_feed()
