# VASP
I'm doing material informatics on my bachelor thesis, here is some code that I write related to VASP mostly, including parser for VASP output file, and machine learning analysis on jupyter notebooks.

## Usage
Create a virtual environment and install required dependencies using `$ pip install -r requirements.txt` and you're good to go.

## Parser Usage
Run `$ python parser/cmd.py <structure name>` on structure directory that contains OUTCAR from VASP calculation. 

You'll have atom positions, magnetic moments, energies, and number of electrons on `DATA` file.

## License
Licensed under [The MIT License](https://github.com/maarlf/vasp/blob/master/LICENSE).
