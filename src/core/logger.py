import logging
import os
from src.core.config import settings

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

level = logging.DEBUG if settings.DEBUG else logging.INFO

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=level,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
