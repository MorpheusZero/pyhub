from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Lightweight Python Github Client'
LONG_DESCRIPTION = 'A lightweight Python Github Client that I use for various projects that does very specific things.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pyhub", 
        version=VERSION,
        author="Dylan Legendre",
        author_email="dylanlegendre09@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            "requests"
        ], 
        # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        keywords=['python', 'github'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Linux :: Ubuntu",            
        ]
)