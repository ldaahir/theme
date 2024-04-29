from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in easy_ui/__init__.py
from tijaabo import __version__ as version

setup(
	name="Tijaabo",
	version=version,
	description="for test only",
	author="liban Dahir Hersi",
	author_email="liban@yooltech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)