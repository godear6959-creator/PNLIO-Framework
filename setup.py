from setuptools import setup, find_packages

setup(
    name='pnlio-framework',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Dependencias básicas para PNL, se pueden añadir más según se necesiten
        'nltk',
        'scikit-learn',
    ],
    author='Gonzalo de la Rivera Arellano',
    author_email='godear6959@gmail.com',
    description='Framework de Código Abierto para la PNL Inversa Ontológica (PNLIO) - Herramienta de Discernimiento Humano-IA.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pnlio-framework', # Placeholder, se puede actualizar
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='pnl inversa ontologia ia agente discernimiento lattis',
)
