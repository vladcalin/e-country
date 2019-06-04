from setuptools import setup, find_packages

setup(
    name='e-country',
    description='A graph based entity and resource management system',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'flask',
        'pymongo',
    ],
    entry_points={
        'console_scripts': [
            'ecountry_server = ecountry.server.app:main'
        ]
    }
)
