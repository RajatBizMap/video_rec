from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in video_rec/__init__.py
from video_rec import __version__ as version

setup(
	name="video_rec",
	version=version,
	description="recording",
	author="BizMap",
	author_email="rajat@bizmap.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
