##setup.py
from setuptools import setup, find_packages

import re
import os

DIR = os.path.dirname(os.path.realpath(__file__))
INIT_FILE = os.path.join(DIR, 'docplex_relaxer', '__init__.py')

with open(INIT_FILE, 'r') as f:
    s = f.read()
    VERSION = re.findall(r"__version__\s*=\s*['|\"](.+)['|\"]", s)[0]

setup(name='docplex_relaxer_wrapper',
      version=VERSION,
      author='Yiduo James Zhan',
      author_email='yiduo.james.zhan@monsanto.com',
      packages=find_packages(),
      install_requires=[
          'docplex',
          'pandas'
      ],
      license='Use as you wish. No guarantees whatsoever.',)