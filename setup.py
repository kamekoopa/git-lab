from setuptools import setup, find_packages

version = "0.2.0"

requires = [
    "pyapi-gitlab==6.2.1",
]

with open("README.rst") as f:
    readme = f.read()

setup(
    name="git-lab",
    version=version,
    description="sub-command of git for access to gitlab",
    long_description=readme,
    author="kamekoopa",
    author_email="hogehugo@gmail.com",
    url="https://github.com/kamekoopa/git-lab",
    packages=find_packages(),
    scripts=["git-lab"],
    license="Apache 2.0",
    install_requires=requires,
)
