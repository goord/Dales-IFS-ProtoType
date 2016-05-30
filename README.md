# Dales-IFS-ProtoType
Prototype code for nesting MPI-parallelized dales models into IFS model columns

Usage:
* Install MPI (OpenMPI or mpich)
* Install mpi4py
* In dales, do: mpiexec -n <x> python dales.py, where <x> denotes the number of parallel processes
* In ifs, do: mpiexec -n <x> python ifs.py, where <x> denotes the number of parallel processes
