#!/usr/bin/env python

from setuptools import setup

__version__ = '5.0.0'

setup(
    name='libtcod-cffi',
    version=__version__,
    author='Kyle Stewart',
    author_email='4B796C65+tcod@gmail.com',
    description='A Python cffi port of libtcod.',
    long_description='\n'.join([open('README.rst', 'r').read(),
                                open('CHANGELOG.rst', 'r').read()]),
    url='https://github.com/HexDecimal/libtcod-cffi',
    download_url='https://pypi.python.org/pypi/libtcod-cffi',
    install_requires=[
        'tdl>=4.1.1',
        ],
    license='Simplified BSD License',
    )
