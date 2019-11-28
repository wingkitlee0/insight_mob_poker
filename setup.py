from setuptools import setup, find_packages

setup(
    name="Poker", 
    packages=find_packages(),
    exclude=["old_tests"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
    )