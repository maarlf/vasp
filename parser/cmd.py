"""energy.py
This script will be used as centralized parser, will extract few informatios from OUTCAR
"""

import os
import sys
import position as p
import magmom as m
import energy as e
import toten as t
import nelectrons as n
import merge as me


outcar = 'OUTCAR'
structures = sys.argv[1]

p.position(outcar, 'POS')
m.magmom(outcar, 'MAGMOM')
e.energy(outcar, 'ENERGY')
t.toten(outcar, 'TOTEN')
n.nelectrons(outcar, 'NELECTRONS')
me.merge(structures)

os.system('cat DATA')