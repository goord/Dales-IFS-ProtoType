#!/usr/bin/python

from mpi4py import MPI
from daleslib import init_dales

init_dales(MPI.COMM_WORLD,1)
