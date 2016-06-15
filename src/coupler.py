#!/usr/bin/python

# This is a prototype coupling code.
# Execute this by typing mpiexec -n24 python coupler.py

from mpi4py import MPI
import sys

sys.path.insert(0,'../ifs')
sys.path.insert(0,'../dales')

from ifslib import init_ifs,finalize_ifs
from daleslib import init_dales,finalize_dales

ifsprocs=4
dalesprocs=5
dalesinst=4
dalessteps=100
ifssteps=10

size=MPI.COMM_WORLD.Get_size()
rank=MPI.COMM_WORLD.Get_rank()

totprocs=ifsprocs+dalesinst*dalesprocs
if(size<totprocs):
    if(rank==0):
        print "ERROR: too few processes have been launched...aborting"
    exit(2)

# Initialize
if(rank<ifsprocs):
    # IFS processes
    comm=MPI.COMM_WORLD.Split(0,rank)

    #Inialization:
    init_ifs(comm)

    # comm.Barrier()
    MPI.COMM_WORLD.Barrier()

    if(rank==0):
        print "BARRIER SYNCHRONIZATION"

    # comm.Barrier()
    MPI.COMM_WORLD.Barrier()
    
    # Cleanup:
    finalize_ifs(comm)
else:
    # Dales processes
    drank=rank-ifsprocs
    dalesindex=drank/dalesprocs
    comm=MPI.COMM_WORLD.Split(dalesindex,drank)

    # Initialization:
    init_dales(comm,dalesindex)

    # comm.Barrier()
    MPI.COMM_WORLD.Barrier()

    # comm.Barrier()
    MPI.COMM_WORLD.Barrier()

    # Cleanup:
    finalize_dales(comm,dalesindex)

    comm.Free()
    
