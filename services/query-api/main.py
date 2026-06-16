from fastapi import FastAPI
from opensearch_client import client

app = FastAPI(title="Distributed Log Platform API")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/logs")
def get_logs():

    response = client.search(
        index="logs",
        body={
            "query": {
                "match_all": {}
            },
            "size": 50
        }
    )

    return [
        hit["_source"]
        for hit in response["hits"]["hits"]
    ]


@app.get("/logs/service/{service_name}")
def logs_by_service(service_name: str):

    response = client.search(
        index="logs",
        body={
            "query": {
                "term": {
                    "service.keyword": service_name
                }
            },
            "size": 50
        }
    )

    return [
        hit["_source"]
        for hit in response["hits"]["hits"]
    ]


@app.get("/logs/level/{level}")
def logs_by_level(level: str):

    response = client.search(
        index="logs",
        body={
            "query": {
                "term": {
                    "level.keyword": level
                }
            },
            "size": 50
        }
    )

    return [
        hit["_source"]
        for hit in response["hits"]["hits"]
    ]