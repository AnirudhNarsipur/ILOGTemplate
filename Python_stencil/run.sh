#!/bin/bash

########################################
############# CSCI 2951-O ##############
########################################
E_BADARGS=65


# change this to point to your local installation
# CHANGE it back to this value before submitting
#On Dept Machine
# export CP_SOLVER_EXEC=/local/projects/cplex/CPLEX_Studio221/cpoptimizer/bin/x86-64_linux/cpoptimizer
#On Mac
export CP_SOLVER_EXEC=/Applications/CPLEX_Studio2211/cpoptimizer/bin/x86-64_osx/cpoptimizer
# run the solver
python3 src/main.py 
