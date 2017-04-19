from setuptools import setup

setup(
    name='corneal',
    version='0.1',
    description='Boundary element solver',
    packages=['corneal'],
    install_requires=['numpy'],
    tests_require=['nose'],
    test_suite='nose.collector',
)
