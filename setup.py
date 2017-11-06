#!/usr/bin/env python
import os
from setuptools import setup, find_packages

__version__ = '0.0.1'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='correosexpress',
    version=__version__,
    author='MarcosAguayo',
    author_email='marcos@aguayo.es',
    url="http://marcosaguayo.com/",
    description="Python package for Correos express carrier",
    long_description=read('README.md'),
    download_url="https://github.com/MarcosAguayo/python-correos-express",
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[],
    license='GPL-3',
    extras_require={
    },
)
