from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gates/__init__.py
from gates import __version__ as version

setup(
	name="gates",
	version=version,
	description="gates monitoring",
	author="ahmed",
	author_email="ahmed751995@riseup.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
