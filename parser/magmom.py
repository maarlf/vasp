"""magmom.py
This scripts are created to extract magnetic moments
from OUTCAR file from VASP calculation.

Examples of information that we need to extract:
 magnetization (x)
 
# of ion     s       p       d       tot
----------------------------------------
  1       -0.003  -0.019   0.710   0.688
  2       -0.008  -0.023   0.614   0.583
  3       -0.007  -0.024   0.614   0.583
  4       -0.008  -0.023   0.608   0.577
  5       -0.004  -0.019   0.700   0.677
------------------------------------------------
tot       -0.029  -0.108   3.245   3.108


 magnetization (x)

# of ion       s       p       d       tot
------------------------------------------
    1        0.045   0.057   2.917   3.018
    2        0.045   0.057   2.917   3.018
    3        0.003   0.050  -0.002   0.050
    4        0.003   0.050  -0.002   0.050
    5       -0.001  -0.082   0.006  -0.077
    6       -0.003  -0.073   0.007  -0.069
    7       -0.001  -0.079   0.007  -0.073
    8       -0.001  -0.082   0.006  -0.077
    9       -0.003  -0.073   0.007  -0.069
   10       -0.001  -0.079   0.007  -0.073
--------------------------------------------------
tot          0.084  -0.254   5.869   5.699

Output that we need:
0.688
0.583
0.583
0.577
0.677
3.108
"""
import sys


def magmom(outcar, output):
    tots = []
    separator = '--------------------------------------------------\n'
    top = '------------------------------------------\n'
    read = False
    for line in reversed(open(outcar).readlines()):
        if line.startswith('tot'):
            tots.append(line.split())
            read = True
        if read:
            if line == top:
                read = False
                break
            elif line == separator:
                continue
            else:
                tots.append(line.split())
    tots = tots[1:-1]
    for i in range(0, len(tots)):
        tots[i] = float(tots[i][4])
    with open(output, 'w') as f:
        for t in reversed(tots):
            f.write(''.join(str(t)))
            f.write('\n')
