import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "new_python_package",
    # update version whenever you create a new release
    version = "{{version}}",
    author = "jrmerz",
    description = ("this is a test, this is only a test"),
    license = "MIT",
    keywords = "",
    url = "http://localhost:3000/package/0f80f625-f591-4611-b6ad-0deddbe3fc53",
    packages=[
        'new_python_package',
        'new_python_package.main'
    ],
    package_data={
      'new_python_package' : ['resources/*']
    },
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)