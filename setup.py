from setuptools import setup

setup(name='Interactive Polyscope',
    version='0.1',
    description='Python package that patches the show function of polyscope to enable async calls in Jupyter notebooks.',
    url='',
    author='Ugo Finnendahl',
    author_email='finnendahl@tu-berlin.de',
    license='MIT',
    packages=["interactive_polyscope"],
    install_requires=[
        'ipykernel',
        'polyscope>=2.0.0',
        'nest-asyncio==1.6.0'
    ]
)
