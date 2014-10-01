#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="nagios-plugin-elasticsearch",
    description="An ElasticSearch availability and performance monitoring plugin for Nagios.",
    version="1.0.2",
    packages=[],
    url="https://github.com/CygnusNetworks/nagios-plugin-elasticsearch",
    author="Peter Adam",
    author_email="info@cygusnetworks.de",
    scripts=["check_elasticsearch"],
    license="MIT",
    install_requires=['nagiosplugin'],
)
