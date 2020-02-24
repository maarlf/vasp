"""energy.py
This will extract free energy from OUTCAR file from VASP calculation.

Examples of information that we need to extract:
  FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)
  ---------------------------------------------------
  free  energy   TOTEN  =       -25.570707 eV

Output that we need:
-25.570707
"""
import sys
import re

outcar = sys.argv[1]
output = sys.argv[2]
toten = []
for line in reversed(open(outcar).readlines()):
    if line.startswith('  free  energy   TOTEN'):
        toten = line.split()
        break
with open(output, 'w') as f:
    f.write(toten[4])
    f.write('\n')
