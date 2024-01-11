from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name='myops',
    ext_modules=[
        CppExtension('myops', ['softmax.cpp'], extra_compile_args=['-O3'])
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
