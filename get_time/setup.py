from setuptools import setup, find_namespace_packages

setup(
    name="get_time_package",
    version="0.1",
    description="Show current time",
    author="Margarita Samburova",
    packages=find_namespace_packages(),
    install_requires=[
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "get_time=time_namespace.get_time_package.get_time_module:main",
        ]
    },
    namespace_packages = ['time_namespace']
)