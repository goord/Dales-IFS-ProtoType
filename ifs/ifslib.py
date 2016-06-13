#!/usr/bin/python

from mpi4py import MPI
from time import sleep

def init_ifs(comm):
    rank=comm.Get_rank()
    if(rank==0):
        size=comm.Get_size()
        print "ifs model contains",size,"processes"
    print "this is ifs process",rank

def do_ifs_step():
    sleep(5)

def finalize_ifs(comm):
    rank=comm.Get_rank()
    if(rank==0):
        print "Finalizing ifs..."
