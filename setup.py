from setuptools import setup, find_packages

setup(
    name='hello_python_library',
    version='0.2.2',
    packages=find_packages(),
    package_data={
        'hello_python_library': ['py.typed'],
    },
)
