from setuptools import setup, find_packages

setup(
    name='bitcoin-price-prediction',
    version='0.1',
    packages=find_packages(exclude=['examples']),
    url='https://github.com/stavros0/bitcoin-price-prediction',
    license='MIT',
    author='Stavros Mekesis',
    author_email='mekstav@gmail.com',
    description='Bayesian regression for latent source model and Bitcoin',
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
