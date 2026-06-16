import time
from opensearchpy import OpenSearch

client = None

while client is None:
    try:
        client = OpenSearch(
            hosts=[{"host": "opensearch", "port": 9200}],
            use_ssl=False,
            verify_certs=False
        )

        client.info()

        print("Connected to OpenSearch")

    except Exception as e:
        print(f"Waiting for OpenSearch: {e}")
        time.sleep(5)