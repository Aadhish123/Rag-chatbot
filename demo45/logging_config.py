import logging

def setup_logging():
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
import logging
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)  # ✅ create folder if missing

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
