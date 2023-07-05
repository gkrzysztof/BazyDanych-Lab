import os
import stacja
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(
    name='Stacja Robocza',
    version=stacja.__version__,
    description='Aplikacja do zbierania pomiarów',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python", ],
    author='Krystian Flisak, Krzysztof Góra',
    keywords='python',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dodaj-osobe = stacja.main:command_line_create_osoba',
            'dodaj-pracownika = stacja.main:command_line_create_pracownik',
            'dodaj-licznik = stacja.main:command_line_create_licznik',
            'dodaj-pomiar = stacja.main:command_line_create_pomiar',
            'wygeneruj-dane = stacja.main:command_line_example_data',
            'eksportuj-csv = stacja.main:command_line_export_csv',
        ]
    },
    platforms='any',
)