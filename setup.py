import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="findCPcore",
    version="0.0.12",
    author="Alex Oarga",
    author_email="alex718123@gmail.com",
    description="findCP core package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/findCP/findCPcore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "cobra==0.16.0",
        "depinfo",
        "future",
        "mpmath",
        "numpy>=1.13",
        "optlang>=1.4.2",
        "pandas>=0.17.0",
        "python-dateutil",
        "python-libsbml",
        "python-libsbml-experimental==5.18.0",
        "pytz",
        "ruamel.yaml>=0.15",
        "setuptools",
        "six",
        "swiglpk",
        "sympy",
        "tabulate",
        "xlwt==1.3.0",
	"six",
    ],
    python_requires='>=3.5',
)
