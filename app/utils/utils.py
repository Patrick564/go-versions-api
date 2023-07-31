import requests
from requests import Response

urls = {
    "all_versions": "https://raw.githubusercontent.com/Patrick564/go-versions-scrap/main/data/selected_versions.json",
    "versions": "https://raw.githubusercontent.com/Patrick564/go-versions-scrap/main/data/versions.json",
}


def get_versions_database(content: str) -> str:
    res: Response = requests.get(urls[content])

    return res.text[0][content]
