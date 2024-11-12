from setuptools import setup, find_packages

setup(name='gym_cartlataccel',
      version='1.1',
      packages=find_packages(),
      install_requires=['gymnasium', 'numpy', 'pygame', 'scipy']
)
