from setuptools import find_packages, setup
from typing import List

def get_req(filepath: str) -> List[str]:
    '''
    this function will return a list of requirements
    '''

    req = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name = 'MLProject',
    version='0.0.1',
    author='Harshwardhan',
    author_email='harsh10joshii@gmail.com',
    packages=find_packages(),
    install_requires = get_req('requirements.txt')
)