from io import open
from setuptools import setup

version = '0.1.0'
lon_descr = 'the module downloads the archive with the assembled NEW program from the link, unzips the program and checks the checksum, If everything is OK, the NEW program overwrites the OLD program'

setup(
    name='file_update_lib',
    version = version,

    author='DarkRadish',
    author_email='gridasovalex19032003@gmail.com',

    description='file update library',
    long_description = lon_descr,

    packages=['file_update_lib']
)
