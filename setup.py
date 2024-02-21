from setuptools import setup, find_packages

setup(
    name="sinli",
    version="1.1.4",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typing-extensions==4.1.1",
        "pycountry==17.9.23",
        "dataclasses==0.8; python_version < '3.7'",
    ],
    author="Devcontrol",
    author_email="devcontrol@zici.fr",
    description="Implementation of the SINLI format. It is used in the book sector in Spain to express commercial operations between book sellers, distributors and editors",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6.9",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
    ],
)
