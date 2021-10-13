
from pyomo.environ import *
from pyomo.opt import *
opt = solvers.SolverFactory("glpk")
model = ConcreteModel()

model.x = Var([1,2], within=NonNegativeReals)

model.c3 = Constraint(expr = model.x[2] >= 2)
model.c2 = Constraint(expr = 4*model.x[1] + 3*model.x[2] >= 24)
model.c1 = Constraint(expr = 5*model.x[1] + 2*model.x[2] >= 20)
model.z = Objective(expr = 8*model.x[1] + 12*model.x[2], sense=minimize)


model.dual = Suffix(direction=Suffix.IMPORT)
results = opt.solve(model)
print(f"x values: {model.x.get_values()}")
################# b)
k = [model.c1, model.c2, model.c3]
i=0
for c in k:
    
    print(f"constraint {i+1}: lslack: {c.lslack()}, uslack: {c.uslack()}")
    i+=1
'''
constraint 1: lslack: 0.0, uslack: inf
constraint 2: lslack: 0.0, uslack: inf
constraint 3: lslack: 6.5, uslack: inf
--> these values give lower and upper bounds for our slack variables
'''
################ c) printing dual values
i=0
for c in k:
    print(f"dual of constraint {i+1}: {model.dual[c]}")
    i +=1 
'''
dual of constraint 1: 6.0
dual of constraint 2: 2.0
dual of constraint 3: 0.0
'''
#############d)
dual = ConcreteModel()

dual.y = Var([1,2,3], within=NonNegativeReals)
# since this is a maximization problem, we have to flip our signs
dual.c1 = Constraint(expr = 5*dual.y[1] + 4*dual.y[2] <= 8)
dual.c2 = Constraint(expr = 2*dual.y[1] + 3*dual.y[2] + dual.y[3] <= 12)
dual.z = Objective(expr = 20*dual.y[1] + 24*dual.y[2] + 2*dual.y[3], sense=maximize)

dual.dual = Suffix(direction=Suffix.IMPORT)
results = opt.solve(dual)
print(f"dual values: {dual.y.get_values()}")
ans = dual.y.get_values()
assert model.dual[model.c1] == ans[1]
assert model.dual[model.c2] == ans[2]
assert model.dual[model.c3] == ans[3]
'''dual values: {1: 0.0, 2: 2.0, 3: 6.0}'''

############e)
'''
primal problem: 
let x and y be the cost of number of components manufactured by a company to make a final product.
the cost of this product is equal to 8 * number of components x manufactored + 12 * number of components y manufactured.

however, to create x, 5 hours of production and 4 hours of assembly are required unit
and to create y:      2 hours of production and 3 of assembly are required per unit

due to contract stipulations, workers must work at least more than 20 hours in assembly and more than 24 hours in production [per unit of time]
furthermore, at least 2 units of y have to be manufactured because [the foundries must always be running since starting them up is incredibly 
expensive]

how many components of x and y should be manufactured such that the cost is minimized?

dual problem: 
suppose the company is planning on expanding its operation and has the option to build 1 more foundry that is used to manufacture y. This would mean
that an extra unit of y would have to be manufactured [in the regular production cycle idk i study CS]. You can look at the shadow prices,
in this case taken to mean the partial derivatives w/ respect to the constraints and clearly see how much the cost would increase for small increases
in the dual function. after thorough analysis, you decide it does not make sense to build another foundry, as the cost would increase dramatically!


'''

