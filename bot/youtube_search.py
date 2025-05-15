from youtubesearchpython import VideosSearch

def search_youtube(query):
    search = VideosSearch(query, limit=20)
    results = []
    for v in search.result()["result"]:
        results.append({
            "title": v["title"],
            "url": v["link"]
        })
    return results