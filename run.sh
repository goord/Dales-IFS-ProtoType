#!/bin/bash

cd src
mpiexec -n 24 python coupler.py
cd -
