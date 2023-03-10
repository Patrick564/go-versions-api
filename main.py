import requests, json
from fastapi import FastAPI


app = FastAPI()


@app.get("/api/versions")
async def get_all_versions():
    res = requests.get("https://raw.githubusercontent.com/Patrick564/golang-versions-list/main/data/versions.json")
    content = json.loads(res.text)[0]["versions"]

    result = dict()

    for version in content:
        if version == "archive":
            continue

        result[version] = f"/api/versions/{version}"

    return { "versions": result }


@app.get("/api/versions/{version}")
async def get_selected_version(version: str):
    res = requests.get("https://raw.githubusercontent.com/Patrick564/golang-versions-list/main/data/selected_versions.json")
    all_versions = json.loads(res.text)[0]["all_versions"]

    content = all_versions[version]
    result = []

    for item in content:
        result.append({
            "name":     item["filename"].split("/")[2],
            "download": "https://go.dev" + item["filename"],
            "size":     item["size"],
            "checksum": item["checksum"]
        })

    return result
