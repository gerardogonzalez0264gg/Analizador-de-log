def detect_suspicious_activity(events, threshold=2):
    """Detect IP addresses with repeated failed login attempts."""

    failed_attempts = {}

    for event in events:
        if event["status"] == "failed":
            ip = event["ip"]

            if ip not in failed_attempts:
                failed_attempts[ip] = 0

            failed_attempts[ip] += 1

    alerts = []

    for ip, attempts in failed_attempts.items():
        if attempts >= threshold:
            alerts.append({
                "ip": ip,
                "failed_attempts": attempts,
                "alert": "Multiple failed login attempts"
            })

    return alerts
    
