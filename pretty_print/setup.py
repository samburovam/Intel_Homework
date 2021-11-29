from setuptools import setup

setup(
    name="pp_package",
    version="0.1",
    description="Show current time",
    author="Margarita Samburova",
    packages=[
        "time_namespace.pp_package",
    ],
    install_requires=[
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "get_time_pp=time_namespace.pp_package.pp_module:pretty_print",
        ]
    },
    namespace_packages=['time_namespace']
)
