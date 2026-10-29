from setuptools import find_packages, setup

setup(
    name="SandboxEnvironment",
    version="0.1",
    packages=find_packages(include=["sandboxenvironment", "sandboxenvironment.*"]),
)
