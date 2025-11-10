import os
from setuptools import  setup, find_packages

NAME = 'pygame_sl'
VERSION = '0.1.0'
DESC = 'A DSL for generating python games using pygame library'
AUTHOR = 'Dejan Sorgic'
AUTHOR_EMAIL = 'dejans1224@gmail.com'
URL = 'https://github.com/DejanS24/pygame_sl'
LICENSE = 'MIT'
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    long_description=README,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'textX>=3.0.0',
        'Jinja2>=3.0.0',
        'pygame>=2.0.0'
    ],
    python_requires='>=3.8',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'textx = textx.cli:textx'
        ],
        'textx_generators': [
            'pygame_sl_python = generator:generate'
        ],
        'textx_languages': [
            'pygame_sl = lang:pygame_sl_lang'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Natural Language :: English',
    ],
    keywords='dsl textx pygame game-development code-generation platformer',
    project_urls={
        'Bug Reports': 'https://github.com/DejanS24/pygame_sl/issues',
        'Source': 'https://github.com/DejanS24/pygame_sl',
        'Documentation': 'https://github.com/DejanS24/pygame_sl/tree/main/docs',
    },
)
