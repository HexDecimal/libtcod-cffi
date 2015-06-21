#!/usr/bin/env python

from setuptools import setup

setup(
    name='libtcod-cffi',
    version=open('tcod/version.txt', 'r').read(),
    author='Kyle Stewart',
    author_email='4B796C65+pythonTDL@gmail.com',
    description='A direct python-cffi port libtcod.',
    long_description='\n'.join([open('README.rst', 'r').read(),
                                open('CHANGELOG.rst', 'r').read()]),
    url='https://github.com/HexDecimal/libtcod-cffi',
    download_url='https://pypi.python.org/pypi/libtcod-cffi',
    packages=['tcod'],
    package_data={'tcod': ['*.txt', '*.rst', 'lib/*.txt',
                           'lib/win32/*',
                           'lib/darwin/*.dylib',
                           'lib/linux*/*']},
    setup_requires=["cffi>=1.1.0"],
    cffi_modules=["build_libtcod.py:ffi"],
    install_requires=["cffi>=1.1.0",
                      "setuptools>=17.1.0"],
    classifiers=['Development Status :: 5 - Production/Stable',
               'Environment :: Win32 (MS Windows)',
               'Environment :: MacOS X',
               'Environment :: X11 Applications',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Natural Language :: English',
               'Operating System :: POSIX',
               'Operating System :: MacOS',
               'Operating System :: Microsoft :: Windows',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.2',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: Implementation :: CPython',
               'Programming Language :: Python :: Implementation :: PyPy',
               'Topic :: Games/Entertainment',
               'Topic :: Multimedia :: Graphics',
               'Topic :: Software Development :: Libraries :: Python Modules',
               ],
    keywords = 'roguelike roguelikes cffi ASCII ANSI Unicode libtcod noise fov heightmap namegen',
    platforms = ['Windows', 'Mac OS X', 'Linux'],
    license = 'Simplified BSD License'
    )
