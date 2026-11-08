def read_log_file(file_path):
    """
    Lee un archivo de registro y devuelve sus líneas.
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
