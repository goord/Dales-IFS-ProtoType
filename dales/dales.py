#!/usr/bin/python

# This is a mockup of the dales program.

from mpi4py import MPI
from daleslib import init_dales

init_dales(MPI.COMM_WORLD,1)
