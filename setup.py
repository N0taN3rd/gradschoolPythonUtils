import os
from setuptools import setup, find_packages

setup(
    name='gradschool',
    version='1.0.0',
    description='The grad students utility belt and then some',
    license='MIT',
    author='John Berlin',
    author_email='n0tan3rd@gmail.com',
    zip_safe=True,
    packages=find_packages(),
    python_requires='>=3.5'
)
