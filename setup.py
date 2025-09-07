import os
import setuptools
from packaging.requirements import Requirement

if __name__ == '__main__':
    with open('requirements.txt') as f:
        file_content = f.read()

    install_requires = [str(Requirement(line)) for line in file_content.splitlines() if line.strip()]

    packages = []
    for path, directories, filenames in os.walk('areator'):
        if '__pycache__' not in path:
            packages.append(path)

    setuptools.setup(
        long_description='',
        name='areator',
        version='0.0.0',
        description='Area calculator package',
        python_requires='==3.*,>=3.8.0',
        author='Malia Skeleton',
        author_email='mskeleto@student.21-school.ru',
        packages=packages,
        include_package_data=True,
        install_requires=install_requires
    )