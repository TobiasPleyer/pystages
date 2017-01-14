# -*- coding: utf-8 -*-
"""
stages
~~~~~~

Simple command line tool to run scripts in a
sequential manner.

Nutshell
--------

Here a small example of a Jinja2 template::

    >>> from stages import Runner
    >>> runner = Runner("config_file", heading="Example run")
    >>> runner.run()

:copyright: (c) 2017 by Tobias Pleyer
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup


setup(
    name='stages',
    version='1.0.dev',
    license='BSD',
    author='Tobias Pleyer',
    description='Simple support for sequential execution of scripts.',
    long_description=__doc__,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Release',
        'Topic :: Deployment',
        'Topic :: Software Development',
    ],
    packages=['stages'],
    install_requires=['colorama'],
    include_package_data=True
)
