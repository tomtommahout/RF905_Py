from distutils.core import setup, Extension
 
module1 = Extension('spi', sources = ['spi.c'])
 
setup (name = 'rf905_py',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [module1])
