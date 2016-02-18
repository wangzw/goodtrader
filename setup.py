import sys
from setuptools import setup, find_packages


setup(
    name='trade',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages("src"),
    url='https://github.com/wangzw/trade',
    license='MIT',
    author='Zhanwei Wang',
    author_email='wangzw@wangzw.org',
    description='Just for fun',
    long_description=open('README.md').read() +
    '\n\n' + open('CHANGELOG.md').read(),
    install_requires=['docopt>=0.6.1', 'coverage>=3.6', 'pandas>=0.16',
                      'tushare>=0.36', 'SQLAlchemy>=1.0.8', 'PyYAML>=3.11', 'pulsar>=1.0.3'],
    tests_require=['pytest'],
    test_suite="tests",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Office/Business :: Financial :: Investment',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
