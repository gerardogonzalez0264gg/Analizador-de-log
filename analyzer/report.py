import os


def generate_report(events, alerts):
    """Generate a text report with the analysis results."""

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/security_report.txt"

    failed = sum(1 for event in events if event["status"] == "failed")
    successful = sum(1 for event in events if event["status"] == "success")

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("LOG ANALYZER - SECURITY REPORT\n")
        file.write("=" * 35 + "\n\n")

        file.write(f"Total events analyzed: {len(events)}\n")
        file.write(f"Failed logins: {failed}\n")
        file.write(f"Successful logins: {successful}\n")
        file.write(f"Security alerts: {len(alerts)}\n\n")

        file.write("SUSPICIOUS ACTIVITY\n")
        file.write("-" * 35 + "\n")

        if alerts:
            for alert in alerts:
                file.write(f"IP: {alert['ip']}\n")
                file.write(f"Failed attempts: {alert['failed_attempts']}\n")
                file.write(f"Alert: {alert['alert']}\n\n")
        else:
            file.write("No suspicious activity detected.\n")

    print(f"Reporte generado: {report_path}")
