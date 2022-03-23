
def manifestFile(name = 'odoo_module', 
                author = 'Unknow',
                category='Uncategorized', 
                version="0.1", ):
    header = '# -*- coding: utf-8 -*-'
    file =  f'''
    'name': "{name}",

    'author': "{author}",

    'category': "{category}",
    'version': "{version}",

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
    '''
    manifest = header +"\n{\n" + file + "\n}"

    return manifest