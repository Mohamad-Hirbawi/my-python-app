import os
import validators
from dotenv import load_dotenv
from logger import setup_logger

load_dotenv()

env = os.getenv("ENV", "dev")
endpoint_url = os.getenv("ENDPOINT_URL")

if env not in ["dev", "release"]:
    env = "dev"

if not validators.url(endpoint_url):
    raise ValueError(f"Invalid URL: {endpoint_url}")

logger = setup_logger(env)

logger.info(f"Current environment: {env}")
logger.info(f"Endpoint URL: {endpoint_url}")
