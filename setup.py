from pathlib import Path

from setuptools import find_packages, setup

PACKAGE_NAME = "netbox_vulnerabilities_page"


def get_version():
    version_file = Path(__file__).parent / PACKAGE_NAME.replace("-", "_") / "version.py"
    with version_file.open() as f:
        for line in f.readlines():
            if "__version__" not in line:
                continue
            delimiter = "'" if "'" in line else '"'
            return line.split(delimiter)[1]
    raise RuntimeError("Could not find the version number")


setup(
    name=PACKAGE_NAME,
    version=get_version(),
    description="An example NetBox plugin",
    url="https://github.com/Daelin148/netbox_vulnerabilities_page",
    author='Me',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)