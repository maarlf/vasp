"""position.py
This scripts will extract atoms position from OUTCAR file from VASP calculation.

Examples of information that we need to extract from Ni100_Clean_rel:
 POSITION                                       TOTAL-FORCE (eV/Angst)
 -----------------------------------------------------------------------------------
      0.00000      0.00000      0.00000         0.000000      0.000000      0.398756
      0.00000      1.76500      1.76500         0.000000      0.000000     -0.393048
      0.00000      0.00000      3.53000         0.000000      0.000000     -0.006319
      0.00000      1.76500      5.30196         0.000000      0.000000     -0.000021
      0.00000      0.00000      6.98746         0.000000      0.000000      0.000632
 -----------------------------------------------------------------------------------
    total drift:                               -0.000038     -0.000038      0.004794

Output that we need:
0.00000      0.00000      0.00000
0.00000      1.76500      1.76500
0.00000      0.00000      3.53000
0.00000      1.76500      5.30196
0.00000      0.00000      6.98746
"""
import sys


def position(outcar, output):
    pos = []
    separator = ' -----------------------------------------------------------------------------------\n'
    read = False
    for line in reversed(open(outcar).readlines()):
        if line.startswith('    total drift:'):
            read = True
            continue
        if read:
            if line.startswith(' POSITION'):
                read = False
                break
            else:
                pos.append(line.split())
    pos = pos[1:-1]
    for i in range(0, len(pos)):
        pos[i] = [float(pos[i][j]) for j in range(0, 3)]
    with open(output, 'w') as f:
        for p in reversed(pos):
            f.write(' '.join(str(x) for x in p))
            f.write('\n')