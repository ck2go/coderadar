from setuptools import setup, find_packages

setup(name='coderadar',
      version='0.0.2',
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['coderadar=coderadar.coderadar:main'],
          }

     )
