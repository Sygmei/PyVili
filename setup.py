import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
if here not in sys.path:
    sys.path.insert(0, here)

import PyVili

with open(os.path.join(here, 'README.rst')) as fp:
    readme = fp.read().strip()

readme_lines = readme.splitlines()

setup(
    name='PyVili',
    packages=find_packages(),
    package_data={'': ['../README.rst']},
    install_requires=[
    ],
    version=PyVili.__version__,
    author='Sygmei',
    author_email='sygmei@obengine.io',
    description=readme_lines[3],
    url='https://github.com/Sygmei/PyVili',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)