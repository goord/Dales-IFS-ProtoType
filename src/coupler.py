#!/usr/bin/python

# This is a prototype coupling code.
# Execute this by typing mpiexec -n24 python coupler.py

from mpi4py import MPI
import sys

sys.path.insert(0,'../ifs')
sys.path.insert(0,'../dales')

from ifslib import init_ifs,finalize_ifs, do_ifs_step
from daleslib import init_dales,finalize_dales, do_dales_step

ifsprocs=4
dalesprocs=5
dalesinst=4
dalessteps=10
ifssteps=3

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

    # Global barrier to start time stepping:
    MPI.COMM_WORLD.Barrier()
    
    for i in range(0,ifssteps):
        # IFS starts first stepping:
        if(rank==0):
            print "Performing ifs step",i
        do_ifs_step()

        # Barrier to synchronize dales models time stepping:
        MPI.COMM_WORLD.Barrier()

        # Barrier to wait for the dales models to finish their time steps:
        MPI.COMM_WORLD.Barrier()
    
    # Cleanup:
    finalize_ifs(comm)
    comm.Free()

else:
    # Dales processes
    drank=rank-ifsprocs
    dalesindex=drank/dalesprocs
    comm=MPI.COMM_WORLD.Split(dalesindex,drank)

    # Initialization:
    init_dales(comm,dalesindex)

    # Barrier to start looping:
    MPI.COMM_WORLD.Barrier()

    for i in range(0,ifssteps):

        # Barrier to wait for IFS to finish its time step:
        MPI.COMM_WORLD.Barrier()

        for j in range(0,dalessteps):
            if(drank%dalesprocs==0):
                print "Performing step",j+i*dalessteps,"for dales model",dalesindex
            do_dales_step()

        # Barrier to synchronize dales models:
        MPI.COMM_WORLD.Barrier()

    # Cleanup:
    finalize_dales(comm,dalesindex)
    comm.Free()
    
