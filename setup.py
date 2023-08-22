from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
#To autorun setup.py:

def get_requirements(file_path:str)->List[str]:
    '''
    Returns list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        [req.replace("\n","") for req in requirements] #Replace newline with ""

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name="mlproject", #Name of package wanting to be made
    version='0.0.1',
    author="Saahil",
    author_email= "thukralsaahil02@gmail.com",
    packages=find_packages(),
    # install_requires = ['pandas', 'numpy','seaborn']
    install_requires = get_requirements("requirements.txt")
    


)



