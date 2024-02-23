from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
from docplex.cp.config import *
from docplex.cp.model import *
# silence logs
context.set_attribute("log_output", None)




def solveAustraliaBinary_example():
    Colors = ["red", "green", "blue"]
    try: 
        cp = CpoModel() 
        
        WesternAustralia =  integer_var(0,3)
        NorthernTerritory = integer_var(0,3)
        SouthAustralia = integer_var(0,3)
        Queensland = integer_var(0,3)
        NewSouthWales = integer_var(0,3)
        Victoria = integer_var(0,3)
        
        cp.add(WesternAustralia != NorthernTerritory)
        cp.add(WesternAustralia != SouthAustralia)
        cp.add(NorthernTerritory != SouthAustralia)
        cp.add(NorthernTerritory != Queensland)
        cp.add(SouthAustralia != Queensland)
        cp.add(SouthAustralia != NewSouthWales)
        cp.add(SouthAustralia != Victoria)
        cp.add(Queensland != NewSouthWales)
        cp.add(NewSouthWales != Victoria)

        params = CpoParameters(
            Workers = 1,
            TimeLimit = 300,
            SearchType="DepthFirst" 
        )
        cp.set_parameters(params)
        
        sol = cp.solve() 
        if sol.is_solution(): 
            
            print( "\nWesternAustralia:    " + Colors[sol[WesternAustralia]])
            print( "NorthernTerritory:   " +   Colors[sol[NorthernTerritory]])
            print( "SouthAustralia:      " +   Colors[sol[SouthAustralia]])
            print( "Queensland:          " +   Colors[sol[Queensland]])
            print( "NewSouthWales:       " +   Colors[sol[NewSouthWales]])
            print( "Victoria:            " +   Colors[sol[Victoria]])
        else:
            print("No Solution found!");
        
    except Exception as e:
        print(f"Error: {e}")


