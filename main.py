#import json_genarator
from json_genarator import generate_json

#import logging
#import sys

#logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import logging
from logging import config
from datetime import datetime


LOG_DIR = "./logs"
timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

logging.config.fileConfig(
        'logger.ini',
        disable_existing_loggers=False,
        # defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
        defaults={"logfilename": f"{LOG_DIR}/file.log"},
    )

logger = logging.getLogger()


if __name__ == '__main__':
    # import logging.config

    # logging.config.fileConfig('logging_config.conf')
    logger.info('<--> The main page <-->')
    generate_json()
