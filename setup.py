from setuptools import setup, find_packages

VERSION = '0.0.3' 
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
        install_requires=['botcity-framework-web>=0.9.0,<1.0', 'sqlalchemy', 'pandas', 'webdriver-manager>=4.0.2', 'numpy<2', 'undetected-chromedriver==2.1.1'], 
        
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows"
        ]
)
