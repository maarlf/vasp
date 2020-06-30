"""energy.py
This will extract fermi and band energies from OUTCAR file from VASP calculation.

Examples of information that we need to extract:
 BZINTS: Fermi energy: -0.055695; 50.000000 electrons
         Band energy:-106.620542;  BLOECHL correction: -0.111340

Output that we need:
-0.055695
-106.620542
"""
import sys
import re


def energy(outcar, output):
    energy = []
    for line in reversed(open(outcar).readlines()):
        if line.startswith(' BZINTS:'):
            energy.append(line.split())
            break
        if line.startswith('         Band energy:'):
            energy.append(line.split())
    energy = [energy[0][1], energy[1][3]]
    with open(output, 'w') as f:
        for e in reversed(energy):
            e = re.sub('\ |\?|\!|\/|\;|\:|\energy', '', e)
            f.write(''.join(e))
            f.write('\n')
