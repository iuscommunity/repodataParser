from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='repodataParser',
      version=version,
      description="A class for reading a Yum repos primary.xml.gz and returning data",
      long_description="",
      classifiers=[],
      keywords='',
      author='Jeffrey Ness',
      author_email='jeffrey.ness@rackspace.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      test_suite='nose.collector',
      )