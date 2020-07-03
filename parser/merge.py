"""merge.py
This script will generate a line of merged information of atom positions,
magnetic moments, total free energy, fermi and band energy, number of electrons
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

    label = 0 if float(magmoms[-1]) <= 2.5 else 1

    row = [structures] + positions + magmoms + energies + toten + nelectrons + [label]

    with open('DATA', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(row)