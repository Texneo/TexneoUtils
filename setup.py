from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Pacote de Utilitários Texneo'
LONG_DESCRIPTION = 'Pacote contendo métodos úteis para o desenvolvimento de automações na Texneo.'

setup(
    name="TexneoUtils",
    version=VERSION,
    author="Texneo",
    author_email="github@texneo.com",  # removido os "< >"
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/plain",  # recomendado
    packages=find_packages(),
    install_requires=[
        'botcity-framework-web>=0.9.0,<1.0',
        'sqlalchemy',
        'pandas',
        'webdriver-manager>=4.0.2',  # ✅ versão corrigida
        'numpy<2',
        'undetected-chromedriver==2.1.1'
    ],
    keywords=['python', 'automação', 'texneo', 'botcity'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"  # opcional, se for MIT
    ],
    python_requires='>=3.7'
)
