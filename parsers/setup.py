from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("helpers", ["helpers.pyx"])]

setup(
  name = 'MARC to FRBR Redis Parser',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
