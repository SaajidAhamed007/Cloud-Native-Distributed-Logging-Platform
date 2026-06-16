import json
import random
import time
from datetime import datetime, UTC

from kafka import KafkaProducer

producer = None

while producer is None:
    try:
        producer = KafkaProducer(
            bootstrap_servers="kafka:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        print("Connected to Kafka")

    except Exception as e:
        print(f"Waiting for Kafka: {e}")
        time.sleep(5)

events = [
    ("INFO", "deployment started"),
    ("INFO", "deployment completed"),
    ("WARN", "high rollout latency"),
    ("ERROR", "rollout failed"),
]

while True:
    level, message = random.choice(events)

    log = {
        "schema_version": "1.0",
        "service": "deployment-service",
        "event_type": "deployment",
        "level": level,
        "message": message,
        "timestamp": datetime.now(UTC).isoformat()
    }

    print(json.dumps(log), flush=True)

    producer.send("logs.raw", log)
    producer.flush()

    time.sleep(3)