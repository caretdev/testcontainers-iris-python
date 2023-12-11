from setuptools import setup, find_namespace_packages

description = "InterSystems IRIS component of testcontainers-python."

setup(
    packages=find_namespace_packages(),
    description=description,
    long_description=open('README.md').read(),
)
