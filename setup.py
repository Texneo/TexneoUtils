from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Pacote de Utilitários Texneo'
LONG_DESCRIPTION = 'Pacote contendo métodos úteis para o desenvolvimento de automações na Texneo.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="utilstexneo", 
        version=VERSION,
        author="Texneo",
        author_email="<github@texneo.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['botcity-email-plugin', 'botcity-framework-web'], 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows"
        ]
)