from setuptools import setup, find_packages


setup(
    name='ctfdl',
    version='1.0.0',
    author='@xrekkusu',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm',
    ],
    entry_points={
        "console_scripts": [
            'ctfdl = ctfdl.main:main',
        ]
    }
)
