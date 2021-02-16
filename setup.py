import setuptools

with open('README.md') as r:
	long_description = r.read()

setuptools.setup(
	name="json_key_press",
	version="1.0.0",
	author="Hendrik Lankers",
	author_email="hendrik.lankers.hl@googlemail.com",
	description="Tool for compression and decompression of dictionary keys for json transfer over limited networks",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/elsholz/json_key_press",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent"
	],
	python_requires=">=3.5"
)
