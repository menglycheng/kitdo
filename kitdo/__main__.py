import sys
import os
from tarfile import NUL 
import click
from kitdo.manifestTb import manifestFile
# from .classmodule import MyClass
# from .funcmodule import my_function
# author = input("author : ")
# category = input("category : ")
# version = input("version : ")
def createSubDirectory(main_path,directory_name,dir_python):
    for dir in directory_name:
        sub_directory = os.path.join(main_path, dir)
        os.mkdir(sub_directory)
        if dir in dir_python:
            with open(f'{main_path}/{dir}/__init__.py','w') as f: 
                f.write("")
                f.close()

def createMinfest(main_path,module_name,author='',category='',version='1.0'):
    with open(f'{main_path}/__manifest__.py','w') as f: 
        f.write(manifestFile(name=module_name, author=author,category=category ,version=version))

def createInit (main_path,dir_python):
    for dir in dir_python:
        with open(f'{main_path}/__init__.py','a+') as f: 
            f.write(f'from . import {dir} \n')
            f.close()
@click.command()
@click.option('-name', prompt='your module name: ',
              help='name of module')
@click.option('--author',default='' ,prompt='author: ',help='author')
@click.option('--category',default='Uncategorized', prompt='category: ',help='category')
@click.option('--version',default = 1.0, prompt='version: ',help='version')
def main(name, author, category, version):
    parent_dir = '.'
    main_path = os.path.join(parent_dir, name)
    os.mkdir(main_path)
    directory_name = ['views', 'models', 'controllers', 'data', 'report','security','static', 'wizard']
    dir_python = ['models', 'controllers', 'report','wizard']

    createSubDirectory(main_path,directory_name,dir_python)
    createInit(main_path,dir_python)
    createMinfest(main_path, name, author, category, version)

if __name__ == '__main__':
    main()