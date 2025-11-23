from feedreader import fetch_feed
from llmprocessor import summarize_text, hashtagsgeneration
#from twitter_sender import post_to_twitter
#from linkedin_sender import post_to_linkedin
from sheetwriter import writetosheet
#from database import has_been_posted, mark_as_posted

FEEDS = [
    "https://www.wired.com/feed/category/ai/",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://feeds.feedburner.com/venturebeat/ai"
]

def process_feed():
    for feed_url in FEEDS:
        print("\nFetching feed: {}".format(feed_url))
        items = fetch_feed(feed_url)

        for item in items[:3]: 
            summary = summarize_text(item["summary"])
            hashtags = generate_hashtags(item["summary"])
            formatted = format_for_platforms(item["title"], summary, hashtags)


            write_to_sheet({
                "title": item["title"],
                "summary": summary,
                "twitter": formatted["twitter"],
                "linkedin": formatted["linkedin"],
                "instagram": formatted["instagram"],
                "facebook": formatted["facebook"],
                "hashtags": hashtags,
                "link": item["link"]
            })

    print("\nAll posts are ready in the Google Sheet!")

if __name__ == "__main__":
    process_feed()