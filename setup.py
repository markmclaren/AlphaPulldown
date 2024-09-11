from setuptools import find_packages, setup

from alphapulldown import __version__

if __name__ == "__main__":
    setup(
        version=__version__,
        packages=find_packages(),
        include_package_data=True,
        package_data={
            "alphapulldown": [
                "scripts/*"
            ],  # Include all files in the scripts directory
        },
    )
