#!/usr/bin/env python
import sys
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='scrapyx-luminati',
        version='0.1.1',        
        description='Luminati middleware for Scrapy',
        author='Henry B.',
        author_email='tubnd.younet@gmail.com',
        url='https://github.com/tubndgit/scrapyx-luminati',
        download_url = 'https://github.com/tubndgit/scrapyx-luminati/archive/master.zip', 
        packages=['scrapyx_luminati'],
        install_requires = [],
        license='MIT',
        python_requires='>=2.7',
    )