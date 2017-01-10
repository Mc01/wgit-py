import sys
from setuptools import setup, find_packages


args = sys.argv
if len(args) > 1 and args[1] == 'install':
    raise ValueError('Please try: bash install.sh')


description = 'Beautiful project manager living in your shell'
setup(
    name='wgit',
    description=description,
    long_description=description,
    url='https://www.watchgit.com',
    version='1.0',
    author='Mc',
    author_email='phenom.home@gmail.com',
    license='MIT',
    platforms='Any',
    packages=find_packages()
)
