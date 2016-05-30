#!/usr/bin/python

from mpi4py import MPI
from ifslib import init_ifs

init_ifs(MPI.COMM_WORLD)
