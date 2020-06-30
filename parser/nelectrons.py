"""energy.py
This will extract number of electrons from OUTCAR file from VASP calculation.

Examples of information that we need to extract:
   NELECT =      56.0000    total number of electron

Output that we need:
56.0000
"""
import sys
import re


def nelectrons(outcar, output):
  n = []
  for line in reversed(open(outcar).readlines()):
      if line.startswith('   NELECT'):
          n = line.split()
          break
  with open(output, 'w') as f:
      f.write(n[2])