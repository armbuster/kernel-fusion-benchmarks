from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension

setup(
    name='myops',
    ext_modules=[
        CUDAExtension('myops', ['myops/softmax.cu'], extra_compile_args=['-O3'])
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
