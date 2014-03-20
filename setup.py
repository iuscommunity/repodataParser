import setuptools

setuptools.setup(
    name='repodataParser',
    version='0.1',
    description='A class for reading a Yum repos primary.xml.gz and returning data',
    long_description='',
    classifiers=[],
    keywords='',
    author='Jeffrey Ness',
    author_email='jeffrey.ness@rackspace.com',
    url='https://github.com/iuscommunity/repodataParser',
    license='',
    packages=setuptools.find_packages(exclude=['ez_setup', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    test_suite='nose.collector',
)

# vim: set syntax=python sw=4 ts=4 expandtab :
