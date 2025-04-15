from setuptools import setup, find_packages

setup(
    name='ryo',
    version='0.1.0',
    packages=['ryo'],  # Especifica o pacote de nível superior 'ryo'
    package_dir={'ryo': 'ryo'},  # Mapeia o pacote 'ryo' para o diretório 'ryo'
    install_requires=['PyYAML', 'yamale'],
    entry_points={
        'console_scripts': [
            'ryo=ryo.src.cli:main',  # Caminho correto para sua função main
        ],
    },
    author='Seu Nome',
    author_email='seu.email@exemplo.com',
    description='Uma biblioteca Python simples.',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
)