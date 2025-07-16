from setuptools import setup, find_packages
from setuptools.command.install import install
import os

# Script de patch: substitui azureedge.net por microsoft.com após instalação
def patch_webdriver_manager():
    import pathlib

    base_dir = pathlib.Path(__file__).parent
    wdm_path = list(base_dir.rglob("site-packages/webdriver_manager/microsoft.py"))

    if not wdm_path:
        print("Não foi possível encontrar o arquivo microsoft.py para patch.")
        return

    target_file = wdm_path[0]
    print(f"Patching webdriver_manager: {target_file}")

    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()

    if "https://msedgedriver.azureedge.net" in content:
        print("URL antiga identificada.")
    
    content = content.replace(
        "https://msedgedriver.azureedge.net",
        "https://msedgedriver.microsoft.com"
    )

    if "https://msedgedriver.azureedge.net" not in content:
        print("URL antiga removida.")

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)

class PostInstallCommand(install):
    """Comando customizado para rodar patch após instalação."""
    def run(self):
        install.run(self)
        try:
            patch_webdriver_manager()
        except Exception as e:
            print(f"Erro ao aplicar patch: {e}")

VERSION = '0.0.3'
DESCRIPTION = 'Pacote de Utilitários Texneo'
LONG_DESCRIPTION = 'Pacote contendo métodos úteis para o desenvolvimento de automações na Texneo.'

setup(
    name="TexneoUtils",
    version=VERSION,
    author="Texneo",
    author_email="github@texneo.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/plain",
    packages=find_packages(),
    install_requires=[
        'selenium',
        'botcity-framework-web>=0.9.0,<1.0',
        'sqlalchemy',
        'pandas',
        'webdriver-manager=4.0.2',
        'numpy<2',
        'undetected-chromedriver==2.1.1'
    ],
    keywords=['python', 'automação', 'texneo', 'botcity'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
    cmdclass={
        'install': PostInstallCommand
    }
)
