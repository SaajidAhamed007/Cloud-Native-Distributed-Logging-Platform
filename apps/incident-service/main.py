import json
import random
import time
from datetime import datetime, UTC

events = [
    ("INFO", "incident created"),
    ("INFO", "incident acknowledged"),
    ("WARN", "escalation triggered"),
    ("ERROR", "service degraded"),
    ("CRITICAL", "service unavailable"),
    ("INFO", "incident resolved"),
]

while True:
    level, message = random.choice(events)

    log = {
        "schema_version": "1.0",
        "service": "incident-service",
        "event_type": "incident",
        "level": level,
        "message": message,
        "timestamp": datetime.now(UTC).isoformat()
    }

    print(json.dumps(log), flush=True)
    time.sleep(5)