from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Pacote de Utilitários Texneo'
LONG_DESCRIPTION = 'Pacote contendo métodos úteis para o desenvolvimento de automações na Texneo.'

setup(
        name="TexneoUtils", 
        version=VERSION,
        author="Texneo",
        author_email="<github@texneo.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['botcity-email-plugin', 'botcity-framework-web'], 
        
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows"
        ]
)