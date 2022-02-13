from setuptools import setup

setup(name='helloworld_test',
    version='0.1',
    description='Test package to run helloworld',
    author='AS',
    author_email='adityashrinivasan@outlook.com',
    license='MIT',
    packages=['helloworld_test'],
    scripts=['bin/hw_test.py'],
    zip_safe=False)
