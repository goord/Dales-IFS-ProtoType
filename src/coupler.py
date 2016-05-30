#!/usr/bin/python

from mpi4py import MPI
import sys

sys.path.insert(0,'../ifs')
sys.path.insert(0,'../dales')

from ifslib import init_ifs
from daleslib import init_dales

ifsprocs=4
dalesprocs=5
dalesinst=4

size=MPI.COMM_WORLD.Get_size()
rank=MPI.COMM_WORLD.Get_rank()

totprocs=ifsprocs+dalesinst*dalesprocs
if(size<totprocs):
    if(rank==0):
        print "ERROR: too few processes have been launched...aborting"
    exit(2)

if(rank<ifsprocs):
    comm=MPI.COMM_WORLD.Split(0,rank)
    init_ifs(comm)
else:
    drank=rank-ifsprocs
    dalesindex=drank/dalesprocs
    comm=MPI.COMM_WORLD.Split(dalesindex,drank)
    init_dales(comm,dalesindex)
    comm.Free()
