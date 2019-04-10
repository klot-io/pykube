import sys

from setuptools import setup, find_packages


install_requires = [
    "requests>=2.12",
    "PyYAML",
    "six>=1.10.0",
    "tzlocal",
]

if sys.version_info < (3,):
    install_requires.extend([
        "ipaddress",
    ])

setup(
    name="pykube",
    version="0.17",
    description="Python client library for Kubernetes",
    author="Kloud of Things I/O",
    author_email="gaffer.fitch@gmail.com",
    license="Apache",
    url="https://github.com/klot-io/pykube",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
    packages=find_packages(),
    entry_points={
        "httpie.plugins.transport.v1": [
            "httpie_pykube = pykube.contrib.httpie_plugin:PyKubeTransportPlugin"
        ],
    },
    install_requires=install_requires,
    extras_require={
        "gcp": [
            "google-auth",
            "jsonpath-ng",
        ]
    },
)
