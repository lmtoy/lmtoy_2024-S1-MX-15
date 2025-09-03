#! /usr/bin/env python3
#
import os
import sys

from lmtoy import runs

project="2024-S1-MX-15"

# Dictionary of sources, each with a list of obsnum's in this project
# negative obsnums are ignored in the combinations. See also comments.txt
# for obsnum specific comments and parameters!
on = {}

on["WR140_CO"] = \
 [ 139132, 139134, 139136, 139142, 139193, 139197, 139311, 139313, 139315, 139317, 139319, 139368, 139370,
   139915,
   139982, 139983, 139984, 139989, 140001, 140002, 140003, 140071, 140072, 140073, 140077, 140165, 140166, 140167,
   140527,
   140813, 140814,
   140910, 140912,-140914,]

# parameters for the first pass of the pipeline (restart=1 is automatically enforced here)
pars1 = {}

pars1["WR140_CO"] = ""

# parameters for the (optional) second pass of the pipeline (e.g. for bank=0)
pars2 = {}

pars2["WR140_CO"] = ""

# parameters for the (optional) third pass of the pipeline (usually for bank=1)
pars3 = {}

pars3["WR140_CO"] = ""

# Found 1 source(s) for 2024-S1-MX-15

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
