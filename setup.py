#!/usr/bin/env python
import sys

from distutils.core import setup

# If we're on Python 2
install_requires = ['mongoengine>=0.8.6']
if sys.version_info[0] == 2:
    # - then we also require `enum34`
    install_requires += [
        'enum34',
    ]

setup(
    name='extras_mongoengine',
    version='0.1',
    description='MongoEngine Extras - Field Types and any other wizardry.',
    url='https://github.com/MongoEngine/extras-mongoengine/',
    install_requires=install_requires,
    packages=['extras_mongoengine'],
)
