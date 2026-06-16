import json
import random
import time
from datetime import datetime, UTC

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
    time.sleep(3)