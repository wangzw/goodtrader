import sys
from setuptools import setup, find_packages


setup(
    name='trade',
    version='0.1',
    package_dir={'':'src'},
    packages=find_packages("src"),
    url='https://github.com/wangzw/trade',
    license='MIT',
    author='Zhanwei Wang',
    author_email='wangzw@wangzw.org',
    description='Just for fun',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    install_requires=['docopt>=0.6.1', 'coverage>=3.6'],
    tests_require=['pytest'],
    test_suite="tests.test_echo",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Office/Business :: Financial :: Investment',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)