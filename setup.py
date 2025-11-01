from setuptools import setup, find_namespace_packages

description = "InterSystems IRIS component of testcontainers-python."

setup(
    name="testcontainers-iris",
    packages=find_namespace_packages(),
    description=description,
    install_requires=[
        "testcontainers>=4.13.2",
        "sqlalchemy>=1.4.0",
        "sqlalchemy-iris>=0.15.0"
    ],
    python_requires=">=3.7",
)
