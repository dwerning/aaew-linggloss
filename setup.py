
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='aaew-linggloss',
    version='0.0.2',
    description='Library for applying Leipzig Glossing Rules to Thesaurus Linguae Aegyptiae (TLA) lemma occurrences',
    python_requires='==3.*,>=3.7.3',
    author='Dr. Daniel Werning',
    author_email='daniel.werning@bbaw.de',
    packages=['aaew_linggloss', 'aaew_linggloss.tests'],
    package_dir={"": "."},
    package_data={"aaew_linggloss": ["data/*.json"]},
    install_requires=[],
    extras_require={"dev": ["dephell==0.*,>=0.8.3", "ipython==7.*,>=7.9.0", "pytest==5.*,>=5.2.2"]},
)
