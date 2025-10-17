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
   140910, 140912,-140914,
   140960, 140962, 
   141038, 141040, 141135, 141137, 141139, 141143, 141145, 141147, 141153,
   141283, 141285, 141287, 141299, 141301, 141303, 141307, 141423, 141425, 141427, 141431, 141433, 141435, 
   141585, 141587, 141589, 141593, 141595, 141597, 141670, 141672, 141674, 141680, 141683, 141685,]

on["WR140_SB0"] = \
 [ 141764, 141768, 141776, 141856, 141860, 141868, 142048, 142049, 142150, 142154, 142205, 142209, 142217,
   142316, 142322, 142655, 142659, 142744, 142748, 142754,]

on["WR140_SB1"] = \
 [ 141766, 141770, 141778, 141858, 141862, 141870, 142051, 142152, 142156, 142207, 142211, 142219,
   142318, 142324, 142657, 142746, 142750, 142756,]

# parameters for the first pass of the pipeline (restart=1 is automatically enforced here)
pars1 = {}

pars1["WR140_CO"] = ""
pars1["WR140_SB0"] = ""
pars1["WR140_SB1"] = ""

# parameters for the (optional) second pass of the pipeline (e.g. for bank=0)
pars2 = {}

pars2["WR140_CO"] = ""
pars2["WR140_SB0"] = ""
pars2["WR140_SB1"] = ""

# parameters for the (optional) third pass of the pipeline (usually for bank=1)
pars3 = {}

pars3["WR140_CO"] = ""
pars3["WR140_SB0"] = ""
pars3["WR140_SB1"] = ""

# Found 1 source(s) for 2024-S1-MX-15

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
