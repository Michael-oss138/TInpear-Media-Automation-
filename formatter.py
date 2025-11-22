def aformatforplatforms(title, summary, hashtags):
    platforms = {
        "twitter": f"{title}\n{summary[:200]}...\n{hashtags}",
        "linkedin": f"{title}\n{summary}\n{hashtags}",
        "instagram": f"{summary}\n{hashtags}",
        "facebook": f"{title}\n{summary}\n{hashtags}"
    }
    return platforms