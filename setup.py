from setuptools import setup, find_packages

setup(
    name='elastic_manager',
    version='0.1.0-beta',
    description='treamline the process of connecting and interacting with an Elasticsearch instance.',
    author='ARC4D3',
    author_email='repo@arc4d3.com',
    packages=find_packages(),
    install_requires=[
        'logger>=0.1.0-beta',
        'elasticsearch>=7.10.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
