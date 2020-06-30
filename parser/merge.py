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


def merge(structures):
    positions = []
    magmoms = []
    energies = []
    toten = []
    nelectrons = []

    with open('POS') as f:
        for line in f:
            for l in line.split(' '):
                positions.append(l.rstrip())

    with open('MAGMOM') as f:
        for line in f:
            magmoms.append(line.rstrip())

    with open('ENERGY') as f:
        for line in f:
            energies.append(line.rstrip())

    with open('TOTEN') as f:
        for line in f:
            toten.append(line)

    with open('NELECTRONS') as f:
        for line in f:
            nelectrons.append(line)

    label = 0 if magmoms[-1] <= 2.5 else 1

    row = [structures] + positions + magmoms + energies + toten + nelectrons + [label]

    with open('DATA', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(row)