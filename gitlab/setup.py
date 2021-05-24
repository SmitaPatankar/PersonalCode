from setuptools import find_packages, setup
setup(
    name="smita",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "smita=smita_project.smita_script:smita_func"
        ],
    },
)