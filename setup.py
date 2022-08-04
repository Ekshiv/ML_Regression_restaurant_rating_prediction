from setuptools import find_packages, setup
from typing import List

# Declaring variable for setup function
PROJECT_NAME="Restaurant-Rating-Predictor"
AUTHOR="Shivam Singh"
VERSION="0.0.1"
DESCRIPTION="This is a machine learning project that calculate ratings of restaurant based on certain features."
LICENSE="Apache License"

HYPHEN_E_DOT="-e ."

REQUIREMENT_FILE_NAME="requirements.txt"


# function to fetch list of libraries from requirements.txt
def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return a list of required libraries
    mentioned in requirements.txt file.
    
    return list of libraries written in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
name=PROJECT_NAME,
author=AUTHOR,
version=VERSION,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list(),
license=LICENSE
)