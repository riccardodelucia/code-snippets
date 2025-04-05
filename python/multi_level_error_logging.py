import logging

# --- Configurazione logger ---

# Logger tecnico (per debugging interno)
tech_logger = logging.getLogger("tech")
tech_handler = logging.FileHandler("tech.log")
tech_handler.setFormatter(logging.Formatter("[TECH] %(asctime)s - %(levelname)s - %(message)s"))
tech_logger.addHandler(tech_handler)
tech_logger.setLevel(logging.DEBUG)

# Logger applicativo (per operatori o log puliti)
app_logger = logging.getLogger("app")
app_handler = logging.FileHandler("app.log")
app_handler.setFormatter(logging.Formatter("[APP] %(asctime)s - %(levelname)s - %(message)s"))
app_logger.addHandler(app_handler)
app_logger.setLevel(logging.INFO)

# --- Eccezioni personalizzate ---
class LowLevelError(Exception):
    pass

class ApplicationError(Exception):
    pass

# --- Funzione che genera un errore di basso livello ---
def low_level_operation():
    raise LowLevelError("Divisione per zero nel modulo X")

# --- Funzione che gestisce l'errore e rilancia un errore di alto livello ---
def process_data():
    try:
        low_level_operation()
    except LowLevelError as e:
        tech_logger.error("Errore di basso livello rilevato", exc_info=True)
        raise ApplicationError("Errore durante l'elaborazione dei dati") from None

# --- Punto di ingresso dell'applicazione ---
def main():
    try:
        process_data()
    except ApplicationError as e:
        app_logger.error(str(e))  # Stack trace *non* incluso
        print("Errore: qualcosa è andato storto. Contatta l'assistenza.")

# --- Esecuzione ---
if __name__ == "__main__":
    main()
