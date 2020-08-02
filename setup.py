#!/usr/bin/env python
import sys
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='scrapyx-luminati',
        version='0.1.4',        
        description='Luminati middleware for Scrapy',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Henry B.',
        author_email='tubnd.younet@gmail.com',
        url='https://github.com/tubndgit/scrapyx-luminati',
        download_url = 'https://github.com/tubndgit/scrapyx-luminati/archive/master.zip', 
        packages=['scrapyx_luminati'],
        install_requires = [],
        license='MIT',
        python_requires='>=2.7',
    )