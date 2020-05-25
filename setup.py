from distutils.core import setup
import os


setup(
    name='mtranslate',
    packages=['mtranslate'],
    package_data={
        "": ["*.txt", "*.rst"],
    },
    include_package_data=True,
    version='1.6',
    description='Google translate console script with easy to use API',
    author='Arnaud Alies',
    author_email='arnaudalies.py@gmail.com',
    url='https://github.com/mouuff/mtranslate',
    download_url='https://github.com/mouuff/mtranslate/tarball/1.6',
    keywords=['console', 'translate', 'translator', 'simple', 'google', 'language'],
    classifiers=[],
)
