from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='student_perfomance',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/ANEES00/studentperformance',
    license='MIT',
    author='Anees',
    author_email='aneesmohdkp@gmail.com',
    description='test',
    install_requires= get_requirements('requirements.txt')
    )
