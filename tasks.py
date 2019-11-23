#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
from datetime import datetime

from invoke import task

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)


##############################################################
# Common
##############################################################
def get_version():
    """Get version"""
    logger.info('Get version')
    with open('package.json') as fin:
        config = json.load(fin)

        version = config['version']

        return version


@task
def gen_package_dependencies_for_docker(c):
    """Generate package dependencies for Docker"""
    logger.info('Generate package dependencies for Docker')
    with open('package.json') as fin:
        config = json.load(fin)

        new_config = dict()
        new_config['license'] = config['license']
        new_config['dependencies'] = config['dependencies']
        new_config['devDependencies'] = config.get('devDependencies')

        with open('package.docker.json', 'w') as fout:
            json.dump(new_config, fout, sort_keys=True,
                      indent=4, separators=(',', ': '))

    with open('package-lock.json') as fin:
        config = json.load(fin)
        config.pop('version')

        with open('package-lock.docker.json', 'w') as fout:
            json.dump(config, fout, sort_keys=True,
                      indent=4, separators=(',', ': '))
