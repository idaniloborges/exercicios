# 1. Crie um pacote chamado [calculo.py](http://calculo.py) e crie uma função para cada operação: +, -, *, /. Depois chame este pacote com o código ***import calculo*** .

    # Após chame as funções uma a uma passando os parâmetros a e b com os devidos números para operar e veja o resultado

from setuptools import setup, find_packages

setup(
    name='calculo',
    version='0.1',
    packages=find_packages(),
    description='Pacote de exemplo para operações matemáticas.',
    author='Danilo',
    author_email='seuemail@exemplo.com',
    url='https://github.com/seunome/meu_pacote',
)


