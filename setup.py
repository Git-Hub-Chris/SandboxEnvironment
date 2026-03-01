from setuptools import setup, find_packages

setup(
    name='SandboxEnvironment',
    version='0.1',
    packages=find_packages(where='my_package'),
    package_dir={"": "my_package"},
)