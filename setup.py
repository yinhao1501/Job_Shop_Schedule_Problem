#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup, Extension

__version__ = '0.2.0'


class NumpyExtension(Extension):
    # setuptools calls this function after installing dependencies
    def _convert_pyx_sources_to_lang(self):
        import numpy
        self.include_dirs.append(numpy.get_include())
        # include libraries and compile flags if not on Windows
        if os.name != 'nt':
            self.libraries.append('m')
            self.extra_compile_args.append('-ffast-math')
        super()._convert_pyx_sources_to_lang()


ext_modules = [NumpyExtension('JSSP.genetic_algorithm._ga_helpers',
                              ['JSSP/genetic_algorithm/_ga_helpers.pyx']),
               NumpyExtension('JSSP.solution._makespan',
                              ['JSSP/solution/_makespan.pyx']),
               NumpyExtension('JSSP.tabu_search._generate_neighbor',
                              ['JSSP/tabu_search/_generate_neighbor.pyx'])
               ]

setup(
    name='JSSP',
    version=__version__,
    description='Package for solving the job shop schedule problem with sequence dependent set up times.',
    author='Matt McFadden (mcfadd)',
    author_email='mrfadd8@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/mcfadd/Job_Shop_Schedule_Problem',
    license='ISC',
    keywords='Job Shop Schedule Problem',
    classifiers=[
        'LICENSE :: OSI APPROVED :: ISC LICENSE (ISCL)',
        'OPERATING SYSTEM :: POSIX',
        'OPERATING SYSTEM :: UNIX',
        'OPERATING SYSTEM :: WINDOWS',
        'PROGRAMMING LANGUAGE :: Python :: 3.6',
        'PROGRAMMING LANGUAGE :: CYTHON',
        'TOPIC :: SCIENTIFIC/ENGINEERING :: MATHEMATICS',
        'TOPIC :: OFFICE/BUSINESS :: SCHEDULING',
    ],
    setup_requires=['numpy', 'cython'],
    install_requires=['numpy', 'plotly', 'progressbar', 'XlsxWriter'],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    ext_modules=ext_modules,
)
