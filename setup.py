from setuptools import setup, find_packages

setup(
    name="flashpy",
    version="1.0.1",
    packages=find_packages(),
    requires=['colorama'],
    url="https://github.com/aygun-m/flashpy",
    author='aygun-m',
    description='A python package to be used to perform active recall revision & learning'
)