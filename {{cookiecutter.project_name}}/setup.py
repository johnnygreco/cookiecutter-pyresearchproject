#! /usr/bin/env python

# Standard library
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="{{ cookiecutter.project_name }}",
    version='v0.1',
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    packages=["{{ cookiecutter.project_name }}", "{{ cookiecutter.project_name }}.tests"],
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.full_name }}",
    # license="MIT",
    description="{{ cookiecutter.description }}",
    long_description=rd("README.md"),
    package_data={},
    install_requires=[],
    # include_package_data=True,
)
