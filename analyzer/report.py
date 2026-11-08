import os


def generate_report(events, alerts):
    """Genera un informe de texto con los resultados del análisis."""

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/security_report.txt"

    failed = sum(1 for event in events if event["status"] == "failed")
    successful = sum(1 for event in events if event["status"] == "success")

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("ANALIZADOR DE REGISTROS - INFORME DE SEGURIDAD\n")
        file.write("=" * 35 + "\n\n")

        file.write(f"Total de eventos analizados: {len(events)}\n")
        file.write(f"Inicios de sesión fallidos: {failed}\n")
        file.write(f"Inicios de sesión exitosos: {successful}\n")
        file.write(f"Alertas de seguridad: {len(alerts)}\n\n")

        file.write("ACTIVIDAD SOSPECHOSA\n")
        file.write("-" * 35 + "\n")

        if alerts:
            for alert in alerts:
                file.write(f"IP: {alert['ip']}\n")
                file.write(f"Intentos fallidos: {alert['failed_attempts']}\n")
                file.write(f"Alerta: {alert['alert']}\n\n")
        else:
            file.write("No se detectó actividad sospechosa.\n")

    print(f"Reporte generado: {report_path}")
