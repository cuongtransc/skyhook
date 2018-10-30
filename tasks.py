#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

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
    logger.info('Get version')
    with open('package.json') as fin:
        config = json.load(fin)

        version = config['version']

        return version


@task
def gen_package_dependencies_for_docker(c):
    logger.info('Generate packages dependencies for Docker')

    with open('package.json') as fin:
        config = json.load(fin)

        new_config = dict()
        new_config['license'] = config['license']
        new_config['dependencies'] = config['dependencies']
        new_config['devDependencies'] = config['devDependencies']

        with open('package.{}.json'.format('docker'), 'w') as fout:
            json.dump(new_config, fout, sort_keys=True,
                      indent=4, separators=(',', ': '))

    with open('package-lock.json') as fin:
        config = json.load(fin)
        config.pop('version')

        with open('package-lock.docker.json', 'w') as fout:
            json.dump(config, fout, sort_keys=True,
                      indent=4, separators=(',', ': '))