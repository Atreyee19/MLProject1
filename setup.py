from setuptools import find_packages,setup
from typing import List

extra = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
     This function will return all the requirements as List
     
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        
    if extra in requirements:
        requirements.remove(extra)
        
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author='Atreyee Bose',
    author_email="atreyeebose9@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)