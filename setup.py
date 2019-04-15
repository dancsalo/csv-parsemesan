from distutils.core import setup
from setuptools import find_packages


setup(
    name='Parsemesan',
    version='1.0.5',
    description='Parsing Tool',
    author='Automated Insights',
    author_email='contact@automatedinsights.com',
    url='https://www.automatedinsights.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'chardet'
    ],
    test_suite='pytest',
    tests_require=['pytest==3.5.0']
)
