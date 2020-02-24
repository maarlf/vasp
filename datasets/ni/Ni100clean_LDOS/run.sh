#! /bin/bash
export OMP_NUM_THREADS=8

BIN=/export/home/nurix/vasp46/vasp.4.6/vasp

echo "a= $i" ; $BIN
