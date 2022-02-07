from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.exceptions import InstallationError

try:
    requirements = parse_requirements("requirements.txt")
    install_requires = [str(r.req) for r in requirements]
except InstallationError:
    install_requires = []

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="wordlebot",
    version="0.1.0",
    description="Worldle bot that will beat any other worldle bot",
    license="MIT",
    author="Matt Weiss",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description
)
