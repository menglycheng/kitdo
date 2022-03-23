import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent


def read_requirments():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements
DESCRIPTION = ''
# The text of the README file
README = (HERE / "README.md").read_text()
setup(
    name = 'dodo',
    version = '0.0.1',
    author= "mengly",
    author_email='menglycheng2@gmail.com',
    packages = find_packages(),
    description= DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/menglycheng/dodo",
    include_package_data=True,
    install_requires = ["click==7.1.2"],
    keywords= ['odoo', 'odoo module', 'create odoo module'],
     license="MIT",
    classifiers= [
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix'
    ],
     entry_points = {
        'console_scripts': [
            'dodo = dodo.__main__:main'
        ]
    }
 )