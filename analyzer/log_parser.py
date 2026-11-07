import re


def parse_log_line(line):
    """Extract relevant information from a log entry."""

    ip_match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)

    if not ip_match:
        return None

    ip_address = ip_match.group()

    parts = line.split()
    timestamp = " ".join(parts[:3])

    username = None

    user_match = re.search(
        r"(?:Failed password for (?:invalid user )?|Accepted password for |authenticating user )(\S+)",
        line
    )

    if user_match:
        username = user_match.group(1)

    if "Failed password" in line:
        status = "failed"
    elif "Accepted password" in line:
        status = "success"
    else:
        status = "other"

    return {
        "timestamp": timestamp,
        "ip": ip_address,
        "username": username,
        "status": status,
        "message": line.strip()
    }
