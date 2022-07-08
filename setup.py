from setuptools import setup, find_packages

setup(name='codemetrics',
      version='0.0.1',
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['codemetrics=codemetrics.code_metrics:main'],
          }

     )
