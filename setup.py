#!/usr/bin/env python

from setuptools import setup

setup(
    name='dog',
    version='0.0.1',
    description='Fetch missing man pages.',
    long_description=open('README.md').read(),
    author='Jeroen Janssens',
    author_email='jeroen@jeroenjanssens.com',
    url='http://dog.rtfd.org/',
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    packages=[
        'dog',
    ],
    entry_points={
        'console_scripts': [
            'dog = dog.cli:main',
        ]
    },
    install_requires=[
        'docopt>=0.6.2',
    ],
)
