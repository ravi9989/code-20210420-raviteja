import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, 'bmi_processor', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='bmi_processor_beta',
    version=get_version(),
    description='This pacakge can process ht wt to bmi and categorise bmi',
    author='Ravi Teja',
    author_email='atmravi395@gmail.com',
    url='https://github.com/ravi9989/code-20210420-raviteja',
    scripts=[],
    packages=find_packages(exclude=['tests*'])
)
