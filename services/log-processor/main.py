import json
import time

from kafka import KafkaConsumer

from processor import enrich_log
from opensearch_client import client

consumer = None

while consumer is None:
    try:
        consumer = KafkaConsumer(
            "logs.raw",
            bootstrap_servers="kafka:9092",
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="earliest",
            group_id="log-processor-group"
        )
        print("Connected to Kafka")

    except Exception as e:
        print(f"Waiting for Kafka: {e}")
        time.sleep(5)

print("Log Processor Started")

for message in consumer:

    log = enrich_log(message.value)

    indexed = False

    while not indexed:
        try:
            client.index(
                index="logs",
                body=log
            )

            indexed = True

        except Exception as e:
            print(f"Waiting for OpenSearch: {e}")
            time.sleep(5)

    print(
        f"Indexed {log['service']} event",
        flush=True
    )