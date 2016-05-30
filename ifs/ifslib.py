#!/usr/bin/python

from mpi4py import MPI

def init_ifs(comm):
    rank=comm.Get_rank()
    if(rank==0):
        size=comm.Get_size()
        print "ifs model contains",size,"processes"
    print "Hello this is ifs proc",rank
