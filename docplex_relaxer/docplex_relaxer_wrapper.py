##docplex_relaxer/docplex_relaxer_wrapper.py
from docplex.mp.relaxer import Relaxer
import pandas as pd

def relax_solve(mdl, prior='named'):
    '''
    mdl:the model
    prior: the specification of how to relax the constraints: 'all' relax all constraints, 'named' relax only named constraints
    :return: relaxed_solution, relaxed_constraints
    '''
    print('\n============================Calling Relaxer=================================\n')
    relax_solve = Relaxer(prioritizer=prior)
    relaxed_solution = relax_solve.relax(mdl)
    print("Number of relaxations:\n",relax_solve.number_of_relaxations)
    relaxed_constraints = relax_solve.relaxations()
    relaxed_constraints = pd.DataFrame.from_dict(relaxed_constraints, orient = 'index').reset_index()
    return relaxed_solution, relaxed_constraints