# -*- coding: utf-8 -*-
"""
stages
~~~~~~

Simple command line tool to run scripts in a sequential manner, written in pure Python.
Basically this script is a very primitive version of what tools like `Jenkins`_ do.
If Jenkins seems like overkill for your needs or you have lots of manual steps interleaved in your automated process, chances are you might find this script useful.

Here a small example of of how to use it in an interpreter session::

    >>> from stages import Runner
    >>> runner = Runner("config_file", heading="Example run")
    >>> runner.run()

Want to read more, found a bug or you want to contribute? Visit the `GitHub repo`_

.. _Jenkins: https://jenkins.io/index.html
.. _GitHub repo: https://github.com/TobiasPleyer/pystages
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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    packages=['stages'],
    install_requires=['configparser', 'colorama'],
    include_package_data=True
)
