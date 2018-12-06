# docplex_relaxer_wrapper
* This module can be used to auto-relax the optimization model to find solutions when encountered infeasibility.
* Official Documentation link: http://ibmdecisionoptimization.github.io/docplex-doc/mp/docplex.mp.relaxer.html
* This function should be called after the model is constructed.

## Install
```python
pip install git+https://github.com/zhanyiduo/docplex_relaxer_wrapper
```
## Input
* mdl: the model to be relaxed
* prior: the specification of how to relax the constraints:
  - 'all' relax all constraints,
  - 'named' relax only named constraints, default.

## Output
* relaxed_solution: the solutions after relaxation. It has the same format as the regular cplex.solve() function't output.
* relaxed_constraints: dataframe containing the all constraints being relaxed.

## Example 
```python
	from docplex_relaxer.docplex_relaxer_wrapper import relax_solve
    model = opt.build_model()
    if not model.solve():
        print('Model infeasible')
        print('Starting Relaxation')
        solution, relaxations = opt.relax_solve(model,'named')
        print(relaxations)
    assert solution, print("Fail to get relaxation")
```