import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="findCPcore",
    version="0.0.2",
    author="Alex Oarga",
    author_email="alex718123@gmail.com",
    description="findCP core package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/findCP/findCPcore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "cobra==0.15.4",
        "depinfo",
        "future",
        "mpmath",
        "numpy",
        "optlang",
        "pandas",
        "python-dateutil",
        "python-libsbml",
        "python-libsbml-experimental",
        "pytz",
        "ruamel.yaml",
        "setuptools",
        "six",
        "swiglpk",
        "sympy",
        "tabulate",
        "xlwt==1.3.0"
    ],
    python_requires='>=3.6',
)
