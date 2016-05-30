#!/usr/bin/python

from mpi4py import MPI

def init_dales(comm,n):
    rank=comm.Get_rank()
    if(rank==0):
        size=comm.Get_size()
        print "dales model",n,"contains",size,"processes"
    print "this is dales model",n,"process",rank
