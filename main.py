
from json_genarator import generate_json


import logging
from logging import config
import pycurl
import certifi
from io import BytesIO

LOG_DIR = "./logs"

logging.config.fileConfig(
        'logger.ini',
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/file.log"},
    )

logger = logging.getLogger()


def curl():
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://host.docker.internal:8000/')
    c.setopt(c.WRITEDATA, buffer)
    # setting the file name holding the certificates
    c.setopt(c.CAINFO, certifi.where())
    # perform file transfer
    c.perform()
    # Ending the session and freeing the resources
    c.close()

    print("asdfasdfasdfasdf", "asdfasdfasdfasdfa", "asdfalkjasdf;lkj;asdf", "<<<=-=-=-=-=-=-=-=-=-=->>>")
    # retrieve the content BytesIO
    body = buffer.getvalue()
    # decoding the buffer
    print("\nCurl:")
    print("<-=-=-=-=-=-\n", "-=-=-=-=-=-", body.decode('iso-8859-1'), "-=-=-=-=-=-\n", "-=-=-=-=-=->")


if __name__ == '__main__':
    import time
    print("before 20")
    time.sleep(20)
    print("after 20")
    logger.info('<--> The main page <-->')
    generate_json()

    curl()

