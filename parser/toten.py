"""energy.py
This will extract total free energy from OUTCAR file from VASP calculation.

Examples of information that we need to extract:
  FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)
  ---------------------------------------------------
  free  energy   TOTEN  =       -25.570707 eV

Output that we need:
-25.570707
"""
import sys
import re


def toten(outcar, output):
  tt = []
  for line in reversed(open(outcar).readlines()):
      if line.startswith('  free  energy   TOTEN'):
          tt = line.split()
          break
  with open(output, 'w') as f:
      f.write(tt[4])