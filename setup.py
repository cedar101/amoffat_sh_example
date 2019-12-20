from setuptools import setup, find_namespace_packages

setup(
    name='mynamespace-subpackage',
    description='',
    long_description='',
    packages=find_namespace_packages(include=['mynamespace.*']),
    zip_safe=False,
)