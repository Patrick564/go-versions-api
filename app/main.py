import requests, json, uvicorn, os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


@app.get("/")
async def redirect_to_versions():
    return RedirectResponse("/api/versions")


@app.get("/api")
async def redirect_api_to_versions():
    return RedirectResponse("/api/versions")

@app.get("/api/docs")
async def swagger_documentation():
    return RedirectResponse("/api/versions")


@app.get("/api/versions")
async def get_all_versions():
    res = requests.get("https://raw.githubusercontent.com/Patrick564/go-versions-scrap/main/data/versions.json")
    content = json.loads(res.text)[0]["versions"]

    result = dict()

    for version in content:
        if version == "archive":
            continue

        result[version] = f"/api/versions/{version}"

    return { "versions": result }


@app.get("/api/versions/{version}")
async def get_selected_version(version: str):
    res = requests.get("https://raw.githubusercontent.com/Patrick564/go-versions-scrap/main/data/selected_versions.json")
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


if __name__ == "__main__":
    port = os.getenv("PORT")

    if port is None:
        port = "8080"

    uvicorn.run(app, host="0.0.0.0", port=int(port))
