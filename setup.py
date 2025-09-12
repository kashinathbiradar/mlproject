from setuptools import find_packages,setup

HY='-e .'
def get_requirements(file_path:str)->list[str]:

 requirements=[]

 with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n"," ") for req in requirements]

    if HY in requirements:
      requirements.remove(HY)

 return requirements



setup(

name='Student_Exam_Performance_Prediction',
version='0.0.1',
author='Kashinath Biradar',
author_email='biradarkashi00@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)
