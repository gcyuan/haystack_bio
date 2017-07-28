#!/usr/bin/env python
"""Description: 
Setup script for Haystack -- Epigenetic Variability and Transcription Factor Motifs Analysis Pipeline
@status:  beta
@version: $Revision$
@author:  Luca Pinello
@contact: lpinello@jimmy.harvard.edu
"""
from __future__ import division, print_function
from setuptools import setup
from distutils.dir_util import copy_tree
import os
import subprocess as sb
import sys

def main():
    setup(
        version="0.5.0",
        name="haystack_bio",
        include_package_data=True,
        packages=["haystack"],
        package_dir={'haystack': 'haystack'},
        package_data={'haystack': ['./*']},
        entry_points={
            "console_scripts": ['haystack_pipeline = haystack.haystack_pipeline_CORE:main',
                                'haystack_hotspots =  haystack.haystack_hotspots_CORE:main',
                                'haystack_motifs = haystack.haystack_motifs_CORE:main',
                                'haystack_tf_activity_plane = haystack.haystack_tf_activity_plane_CORE:main',
                                'haystack_download_genome = haystack.haystack_download_genome_CORE:main', ]
        },
        description="Epigenetic Variability and Transcription Factor Motifs Analysis Pipeline",
        author='Luca Pinello',
        author_email='lpinello@jimmy.harvard.edu',
        url='http://github.com/lucapinello/Haystack',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Programming Language :: Python',
        ],
        install_requires=[]
    )

HAYSTACK_DEPENDENCIES_FOLDER = '%s/haystack_data' % os.environ['HOME']

if not os.path.exists(HAYSTACK_DEPENDENCIES_FOLDER):
    sys.stdout.write('OK, creating the folder:%s' % HAYSTACK_DEPENDENCIES_FOLDER)
    os.makedirs(HAYSTACK_DEPENDENCIES_FOLDER)
else:
    sys.stdout.write('\nI cannot create the folder!\nThe folder %s is not empty!' % HAYSTACK_DEPENDENCIES_FOLDER)


d_path = lambda x: (x, os.path.join(HAYSTACK_DEPENDENCIES_FOLDER, x))

copy_tree(*d_path('haystack_data'))

if __name__ == '__main__':
    main()

    sys.stdout.write('\n\nINSTALLATION COMPLETED, open a NEW terminal and enjoy HAYSTACK!')