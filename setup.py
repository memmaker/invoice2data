# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
version = open('VERSION').read().strip()

setup(
    name='invoice2data',
    version=version,
    author='Manuel Riel',
    author_email='github@snapdragon.cc',
    url='https://github.com/manuelRiel/invoice2data',
    description='Python parser to extract data from pdf invoice',
    license="MIT",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        r.strip() for r in open('requirements.txt').read().splitlines()],
    zip_safe=False
)
