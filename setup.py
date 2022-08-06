from setuptools import setup, find_packages


long_description = open("README.md").read()


setup(name="python-eml",
      version="0.0.1",
      author="Pieter Provoost",
      author_email="pieterprovoost@gmail.com",
      description="Python package containing dataclasses for the Ecological Metadata Language (EML) standard",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/pieterprovoost/python-eml",
      license="MIT",
      packages=find_packages(),
      zip_safe=False
)
