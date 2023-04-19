from setuptools import setup

import recommend

setup(
    name='recommend',
    version=recommend.__version__,
    url='https://github.com/chyikwei/recommend/',
    install_requires=[
        'numpy>=1.11.0',
        'scipy>=0.15.0',
        'six'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    packages=['recommend', 'recommend.utils'],
    description='Simple recommendatnion system implementation with Python'
)
