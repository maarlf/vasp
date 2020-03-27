"""merge.py
This script will generate new csv file from generated
dataset e.g (POS, MAGMOM, ENERGY, TOTEN) and its labels

Examples of information that we need:
POS
0.0 0.0 0.0
0.0 1.765 1.765
0.0 0.0 3.53
0.0 1.765 5.30196
0.0 0.0 6.98746

MAGMOM
0.688
0.583
0.583
0.577
0.677
3.108

ENERGY
-0.055695
-106.620542

TOTEN
-25.570707

CLASS

Output that we need:
One csv file containing all of these informations

atom positions, magnetic moments, magnetic moment total, band, fermi, toten, class

Usage:
./parser/datasets.py <materials> datasets/vasp/<materials>/<materials>.csv
"""
import sys
import csv

materials = sys.argv[1]
output_csv = sys.argv[2]

positions = []
magmoms = []
energies = []
toten = []

dataset_dir = 'datasets/' + materials

with open(dataset_dir + '/POS') as f:
    for line in f:
        positions.append(line.split())

with open(dataset_dir + '/MAGMOM') as f:
    for line in f:
        magmoms.append(line)

with open(dataset_dir + '/ENERGY') as f:
    for line in f:
        energies.append(line)

with open(dataset_dir + '/TOTEN') as f:
    for line in f:
        toten.append(line)

label = 10 if magmoms[-1] <= 2.5 else 1

with open(output_csv) as f:
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
        'x9', 'y9', 'z9',
        'x10', 'y10', 'z10',
        'm1', 'm2', 'm3', 'm4', 'm5', 'mtot',
        'fermi', 'band', 'toten',
        'class'
    ])
    writer.writerow(row)