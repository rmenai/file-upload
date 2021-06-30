from app.apps import logger

try:
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv(), override=True)
    logger.info("Found .env file, loading environment variables from it.")
except ModuleNotFoundError:
    pass
