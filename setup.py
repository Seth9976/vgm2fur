# setup.py(仓库根目录,与 pyproject.toml 同级)  
from setuptools import setup  
from setuptools.extension import Extension  
from Cython.Build import cythonize  
  
setup(ext_modules=cythonize([  
    Extension("vgm2fur.bitfield",            ["vgm2fur/bitfield.py"]),  
    Extension("vgm2fur.vgm.unpacker",        ["vgm2fur/vgm/unpacker.py"]),  
    Extension("vgm2fur.vgm.song",            ["vgm2fur/vgm/song.py"]),  
    Extension("vgm2fur.chips.sn76489",       ["vgm2fur/chips/sn76489.py"]),  
    Extension("vgm2fur.chips.ym2612",        ["vgm2fur/chips/ym2612.py"]),  
    Extension("vgm2fur.chips.sampler",       ["vgm2fur/chips/sampler.py"]),  
    Extension("vgm2fur.transform.tabulate",  ["vgm2fur/transform/tabulate.py"]),  
], language_level=3, compiler_directives={"boundscheck": False, "wraparound": False}))
