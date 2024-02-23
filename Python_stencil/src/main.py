import os
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path

from docplex.cp.config import context

from scheduler import solveAustraliaBinary_example
from model_timer import Timer 


# Stencil created by Anirudh Narsipur February 2023
# Adapted from code written by Alexander Ding and Anirudh Narsipur


#DO NOT change this. Change run.sh to point to your local CPLEX installation
def set_context():
    solver_exec = Path(os.environ["CP_SOLVER_EXEC"])
    if not solver_exec.exists():
        print("Error: Set CP Solver Exec\n")
        exit(1)
    print(f"Using cp installation at {solver_exec}")
    context.solver.agent = "local"
    context.solver.local.execfile = str(solver_exec)




def main():
    set_context()
    solveAustraliaBinary_example()


if __name__ == "__main__":
    main()
