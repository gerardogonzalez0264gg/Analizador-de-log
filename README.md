# Log Analyzer

Proyecto de ciberseguridad desarrollado en Python para analizar registros de autenticación e identificar actividades sospechosas, como múltiples intentos fallidos de inicio de sesión.

## Características

- Lectura de archivos de registros (logs).
- Extracción de fechas, direcciones IP, nombres de usuario y estados de autenticación.
- Detección de múltiples intentos fallidos de inicio de sesión.
- Identificación de direcciones IP sospechosas.
- Generación automática de informes de seguridad en formato TXT.

## Tecnologías utilizadas

- Python 3
- Linux
- Expresiones regulares (Regex)
- Git y GitHub

## Estructura del proyecto

```text
LOG-ANALYZER/
├── analyzer/
│   ├── __init__.py
│   ├── log_reader.py
│   ├── log_parser.py
│   ├── detector.py
│   └── report.py
├── samples/
│   └── auth.log
├── reports/
├── main.py
├── .gitignore
└── README.md
```

## Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/gerardogonzalez0264gg/Analizador-de-log
cd Analizador-de-log
```

Crear y activar un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Ejecutar el analizador:

```bash
python main.py
```

## Funcionamiento

El proyecto analiza registros de autenticación y procesa cada entrada para extraer información relevante.

Posteriormente, identifica direcciones IP que registran dos o más intentos fallidos de inicio de sesión y genera alertas cuando se cumple esta condición.

Finalmente, crea un informe con estadísticas de los eventos analizados y las actividades sospechosas detectadas.

## Objetivos de aprendizaje

Este proyecto permite poner en práctica conocimientos de:

- Programación con Python.
- Análisis de registros en Linux.
- Expresiones regulares.
- Detección básica de actividades sospechosas.
- Automatización de tareas de ciberseguridad.

## Aviso

Proyecto desarrollado con fines educativos. Los registros utilizados para las pruebas contienen datos ficticios y no representan actividad real.

No reemplaza las herramientas profesionales de monitoreo y detección de amenazas.
