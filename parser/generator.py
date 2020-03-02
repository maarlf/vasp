"""generator.py
Generate 100 of dummy data for designing a model

Features that we need:

- atom positions (x, y z), 10 atoms each: 30 cols [0, 2]
- magnetic moments: 5 cols [0.5, 0.6]
- total of magnetic moment: 1 cols 
- band energy: 1 cols [-0.5, -0,6]
- fermi energy: 1 cols [-100, -110]
- toten: 1 cols [-0, -20]

Label:

- class: 1 cols

Usage:
./parser/generator.py <n> <output_file>
"""
import sys
import csv
import numpy as np

n = int(sys.argv[1])
output_file = sys.argv[2]

data = []

for i in range(0, n):
    pos = np.random.uniform(0, 2, size=(1, 30))
    magmom = np.random.uniform(0, 1, size=(1, 5))
    mtot = np.sum(magmom)
    band = np.random.uniform(-0.5, 1)
    fermi = np.random.uniform(-50, -150)
    toten = np.random.uniform(0, -50)
    label = 0 if mtot <= 2.5 else 1
    row = pos[0].tolist() + magmom[0].tolist() + [mtot, band, fermi, toten, label]
    data.append(row)

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow([
        'x1', 'y1', 'z1',
        'x2', 'y2', 'z2',
        'x3', 'y3', 'z3',
        'x4', 'y4', 'z4',
        'x5', 'y5', 'z5',
        'x6', 'y6', 'z6',
        'x7', 'y7', 'z7',
        'x8', 'y8', 'z8',
        'x8', 'y9', 'z9',
        'x10', 'y10', 'z10',
        'm1', 'm2', 'm3', 'm4', 'm5', 'mtot'
        'fermi', 'band', 'toten',
        'class'])
    for row in data:
        writer.writerow(row)
    