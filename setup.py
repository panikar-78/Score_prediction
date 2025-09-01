from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    It will return the list of requirements
    '''
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("\n","") for r in req]

        if hypen_e_dot in req:
            req.remove(hypen_e_dot)

        return req

setup(
    name ='mlporject',
    version = '0.0.1',
    author = 'Panikar',
    author_email = 'panikar.dev78@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)