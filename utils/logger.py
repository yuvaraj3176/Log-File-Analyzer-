import logging
from config import APP_LOG_FILE

def setup_logger():
    logging.basicConfig(
        filename=APP_LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
