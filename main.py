from analyzer.log_reader import read_log_file
from analyzer.log_parser import parse_log_line
from analyzer.detector import detect_suspicious_activity
from analyzer.report import generate_report


def main():

    log_file = "samples/auth.log"

    lines = read_log_file(log_file)

    print(f"\nTotal de líneas leídas: {len(lines)}")

    events = []

    for line in lines:
        event = parse_log_line(line)

        if event:
            events.append(event)

    print(f"Eventos analizados: {len(events)}")

    alerts = detect_suspicious_activity(events)

    print(f"Alertas detectadas: {len(alerts)}")

    for alert in alerts:
        print(f"IP sospechosa: {alert['ip']}")
        print(f"Intentos fallidos: {alert['failed_attempts']}")

    generate_report(events, alerts)


if __name__ == "__main__":
    main()
