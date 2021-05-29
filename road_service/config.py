import os
import yaml
import logging

logger = logging.getLogger(__name__)


def configure_app(app):
    app.config["BASE_DIR"] = os.path.dirname(os.path.dirname(__file__))
    app.config["TEMPLATE_FOLDER"] = os.path.join(app.config["BASE_DIR"], 'templates')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["MULTIPLE"] = 2


def load_secrets(base_dir: str):
    secrets_path = os.path.join(base_dir, 'secrets', 'secrets.yaml')
    try:
        with open(secrets_path, 'r') as secrets_file:
            return yaml.load(secrets_file)
    except BaseException as secr_expt:
        logger.error('No secrets found!: {}'.format(secr_expt))
        return {}
