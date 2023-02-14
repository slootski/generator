
from json_genarator import generate_json


import logging
from logging import config


LOG_DIR = "./logs"

logging.config.fileConfig(
        'logger.ini',
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/file.log"},
    )

logger = logging.getLogger()


if __name__ == '__main__':

    logger.info('<--> The main page <-->')
    generate_json()
