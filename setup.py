#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Caixa transactions REST API testing script.


from setuptools import setup, find_packages

import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))
README_PATH = os.path.join(HERE, 'README.md')
CHANGELOG_PATH = os.path.join(HERE, 'CHANGELOG.md')

if not (sys.version_info.major == 3):
    raise RuntimeError('Wrong Python version')

README = open(README_PATH, encoding='utf-8').read()
CHANGELOG = open(CHANGELOG_PATH, encoding='utf-8').read()

setup(
    name='caixab_rest_api',
    author='info@caixab.com',
    version='1.1',
    description='Caixa official rest api python library',
    long_description=README + '\n\n\'' + CHANGELOG,
    long_description_content_type = 'text/markdown',
    keywords='transactions, rest api, caixab, caixa',
    packages=find_packages(exclude=['']),
    include_package_data=True,
    install_requires=[
        'argparse==1.4.0'
        'subprocess==0.0.8'
        'json==1.6.1'
        ],
    zip_safe=False,
    entry_points={
        'console_scripts': ['caixab_rest_api-cli=caixab_rest_api.cli']
        },
    )