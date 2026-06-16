import json

from kafka import KafkaConsumer

from processor import enrich_log

consumer = KafkaConsumer(
    "logs.raw",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="log-processor-group"
)

print("Log Processor Started")

for message in consumer:
    log = message.value

    enriched_log = enrich_log(log)

    print(
        json.dumps(
            enriched_log,
            indent=2
        ),
        flush=True
    )