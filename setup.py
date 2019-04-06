"""Manipulate vili files in Python
"""

from setuptools import setup, find_packages
from os import path

from vili import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vili',
    version=__version__,
    description='PyVili is a Python API to manipulate Vili Data files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sygmei/PyVili',
    author='Sygmei',
    author_email='sygmei@sygmei.io',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='vili data language config',
    packages=find_packages(include=['vili']),
    python_requires='>=3.6, <4',
    install_requires=[],
    extras_require={
        'test': [
            'coverage',
            'tox',
            'pytest',
            'flake8'
        ],
    },
    entry_points={
        'console_scripts': [],
    },
    project_urls={
        'Bug Reports': 'https://github.com/Sygmei/PyVili/issues',
        'Source': 'https://github.com/Sygmei/PyVili',
    },
)
