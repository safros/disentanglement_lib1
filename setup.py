# coding=utf-8
# Copyright 2018 The DisentanglementLib Authors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""setup.py for disentanglement_lib."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='disentanglement_lib',
    version='1.5',
    description=('Library for research on disentangled representations.'),
    author='DisentanglementLib Authors',
    author_email='no-reply@google.com',
    url='http://github.com/google-research/disentanglement_lib',
    license='Apache 2.0',
    packages=find_packages(),
    include_package_data=True,
    scripts=[
        'disentanglement_lib/bin/dlib_aggregate_results',
        'disentanglement_lib/bin/dlib_reproduce',
        'disentanglement_lib/bin/dlib_reason',
        'disentanglement_lib/bin/dlib_visualize_dataset',
        'disentanglement_lib/bin/dlib_evaluate',
        'disentanglement_lib/bin/dlib_udr',
        'disentanglement_lib/bin/dlib_postprocess',
        'disentanglement_lib/bin/dlib_train',
        'disentanglement_lib/bin/dlib_visualize_dataset',
        'disentanglement_lib/bin/dlib_visualize_model',
        'disentanglement_lib/bin/dlib_tests',
        'disentanglement_lib/bin/dlib_download_data',
        'disentanglement_lib/bin/dlib_reproduce_jmlr',
        'disentanglement_lib/bin/dlib_reproduce_semi_supervised',
        'disentanglement_lib/bin/dlib_reproduce_weakly_supervised',
        'disentanglement_lib/bin/dlib_train_semi_supervised',
        'disentanglement_lib/bin/dlib_train_weakly_supervised',
    ],
    install_requires=[
        'future',
        'imageio',
        'gin-config',
        'scikit-learn',
        'numpy',
        'pandas',
        'simplejson',
        'six',
        'matplotlib>=1.5.2',
        'pillow>=5.0.0',
        'pandas>=0.23.0',
        'scipy>=1.0.0',
        'tensorflow_hub>=0.2',
        'tensorflow_probability',
        'seaborn',
    ],
    extras_require={
        'tf': ['tensorflow>=1.14'],
        #'tf_gpu': ['tensorflow-gpu>=1.14'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow machine learning disentanglement learning',
)
