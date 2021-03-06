# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rinokeras',
    version='0.1.0',
    description='CannyLab Algorithms Repository',
    long_description=readme,
    author='Roshan Rao',
    author_email='roshan_rao@berkeley.edu',
    url='https://github.com/CannyLab/rl-algs',
    license=license,
    install_requires=[
        'nose >= 1.3.7',
        'numpy >= 1.14.1',
        'tensorflow >= 1.9.0',
    ],
    packages=find_packages(exclude='example')  # exclude=('tests', 'docs')
)
