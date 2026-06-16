from datetime import datetime, UTC


def enrich_log(log: dict) -> dict:
    log["processed_at"] = datetime.now(UTC).isoformat()
    log["pipeline_version"] = "1.0"

    return log