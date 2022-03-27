#!/usr/bin/env python3

version = "1.0.5"

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='ngflask',  # Required
    version=version,  # Required
    description='File-sharing tool',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/cyberhexe/ngflask',  # Optional
    author='totekuh',  # Optional
    author_email='totekuh@protonmail.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',

        'License :: OSI Approved :: MIT License',

        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='file-sharing, ngrok, flask',  # Optional
    package_dir={'': './src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.6, <4',
    install_requires=[
        "flask",
        'flask-autoindex',
        "pyngrok"
    ],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'ngflask=ngflask.flask_ngrok:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/cyberhexe/ngflask/issues',
        'Source': 'https://github.com/cyberhexe/ngflask',
    },
)