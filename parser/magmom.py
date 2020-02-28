"""magmom.py
This scripts are created to extract atoms position
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

Output that we need:
0.688
0.583
0.583
0.577
0.677
3.108
"""
import sys

outcar = sys.argv[1]
output = sys.argv[2]
tots = []
separator = '------------------------------------------------\n'
read = False
with open(outcar, 'r') as f:
    for line in f:
        if line.startswith(' magnetization (x)'):
            read = True
            f.next()
        if read:
            if line == separator:
                continue
            if line.startswith('tot'):
                tots.append(line.split())
                read = False
                break
            else:
                tots.append(line.split())
tots = tots[3:]
for i in range(0, len(tots)):
    tots[i] = float(tots[i][-1])
with open(output, 'w') as f:
    for t in tots:
        f.write(''.join(str(t)))
        f.write('\n')
