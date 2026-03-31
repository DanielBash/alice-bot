""" - Code running after app initialization
 - Final setup"""


# -- importing modules
import settings
from flask import current_app
from .. import models
from core.logger import log


def main():
    log.info('Running post-innit')


if __name__ == '__main__':
    main()
