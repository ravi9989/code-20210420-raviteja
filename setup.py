import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
    'json',
    'functools',
    'bisect'
]


def get_version():
    init = open(os.path.join(ROOT, 'event_handler', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='bmi_processor',
    version=get_version(),
    description='This pacakge can process ht wt to bmi and categorise bmi',
    author='Ravi Teja',
    author_email='atmravi395@gmail.com',
    url='git@github.com:eunimart/vdezi_event_handler.git',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    install_requires=requires,
    license='unlicense',
    classifiers=[
        'Development Status :: 1 - Production/Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)