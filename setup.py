# -------------------------------------------------------------
#	This script is for creating compiling the C
#	source file using Cython
# -------------------------------------------------------------

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("listWriter.pyx")
)
