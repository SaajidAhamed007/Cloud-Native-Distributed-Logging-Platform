import json
import random
import time
from datetime import datetime, UTC

events = [
    ("INFO", "metrics collection started"),
    ("INFO", "metrics collection completed"),
    ("WARN", "cpu usage exceeded threshold"),
    ("WARN", "memory usage exceeded threshold"),
    ("ERROR", "node unreachable"),
    ("ERROR", "prometheus scrape failed"),
]

while True:
    level, message = random.choice(events)

    log = {
        "schema_version": "1.0",
        "service": "monitoring-service",
        "event_type": "monitoring",
        "level": level,
        "message": message,
        "timestamp": datetime.now(UTC).isoformat()
    }

    print(json.dumps(log), flush=True)
    time.sleep(4)