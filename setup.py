from setuptools import setup

VERSION='0.1.002'
INSTALL_REQUIRES=[]
with open('requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name='deb_pkg_utils',
    version=VERSION,
    packages=[''],
    url='',
    license='Apache 2.0',
    author='Edward HHA Law',
    author_email='',
    description='Demo Project for Career.',
    install_requires=INSTALL_REQUIRES,
    package_data={'': ['requirements.txt']}
)
