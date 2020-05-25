from distutils.core import setup
import os
import sys

data_dir = os.path.join(sys.prefix, "local/lib/python3.7/dist-package/mtranslate")
setup(
    name='mtranslate',
    packages=['mtranslate'],
    package_data={
        "": ["*.txt", "*.rst"],
        "mtranslate": ["*.txt"],
    },
    data_files=[("mtranslate", [os.path.join(data_dir, "mydata")])],
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
