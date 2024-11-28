import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
logger.level = logging.INFO


class Config:
    database_name = "quiz_db.sqlite"


config = Config()
