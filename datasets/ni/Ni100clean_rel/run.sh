#! /bin/bash
export OMP_NUM_THREADS=8
BIN=/export/home/nurix/vasp46/vasp.4.6/vasp
rm WAVECAR
echo "a= $i" ; $BIN
done
