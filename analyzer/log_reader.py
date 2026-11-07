def read_log_file(file_path):
    """
    Read a log file and return its lines.
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo: {file_path}")
        return []

    except PermissionError:
        print(f"Error: No tienes permisos para leer: {file_path}")
        return []
