from setuptools import setup, find_packages

def read_requirments():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements
DESCRIPTION = ''
setup(
    name = 'dodo',
    version = '0.0.1',
    author= "mengly",
    author_email='menglycheng2@gmail.com',
    packages = find_packages(),
    description= DESCRIPTION,
    include_package_data=True,
    install_requires = ["click==7.1.2"],
    keywords= ['odoo', 'odoo module', 'create odoo module', ''],
    classifiers= [
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