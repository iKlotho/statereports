# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requires = f.readlines()

setup(
    name='statereports',
    version='0.0.1',
    description=u'Scraping State Reports from ic3.gov',
    long_description=readme,
    author=u'Umut Kahrıman',
    author_email=u'umutkahrimanedu@gmail.com',
    url=u'https://github.com/iklotho/statereport',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requires
)
