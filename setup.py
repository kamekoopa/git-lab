from setuptools import setup, find_packages

version = "0.1.0"

requires = [
    "pyapi-gitlab==6.1.6",
]

setup(
    name="git-lab",
    version=version,
    description="sub-command of git for access to gitlab",
    author="kamekoopa",
    author_email="hogehugo@gmail.com",
    url="",
    packages=find_packages(),
    scripts=["git-lab"],
    install_requires=requires,
)
