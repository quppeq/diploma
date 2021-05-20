import os
import yaml
import logging

logger = logging.getLogger(__name__)


class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_secrets():
    secrets_path = os.path.join(Config.BASE_DIR, 'secrets', 'secrets.yaml')
    try:
        with open(secrets_path, 'r') as secrets_file:
            return yaml.load(secrets_file)
    except BaseException as secr_expt:
        logger.error('No secrets found!: {}'.format(secr_expt))
        return {}


secrets = load_secrets()
