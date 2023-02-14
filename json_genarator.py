import json
import random

import consts

import logging

logger = logging.getLogger(__name__)


def generate_json():
    result = json.dumps(
        {
            'group_name': random.choice(consts.GROUP_NAMES),
            'country_name': random.choice(consts.COUNTRY_NAMES),
            'surname_name': random.choice(consts.SURNAMES_LIST),
            'mail_name': random.choice(consts.MALE_NAMES_LIST),
            'female_name': random.choice(consts.FEMALE_NAMES_LIST),
        }
    )
    logger.info(result)
    return result
