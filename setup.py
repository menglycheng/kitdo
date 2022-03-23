from setuptools import setup, find_packages

def read_requirments():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

setup(
    name = 'dodo',
     version = '0.1.0',
    packages = find_packages(),
    include_package_data=True,
    install_requires = read_requirments()
    entry_points = {
        'console_scripts': [
            'dodo = dodo.__main__:main'
        ]
    })