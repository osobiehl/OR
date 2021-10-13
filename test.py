
from pyomo.environ import *
from pyomo.opt import *
opt = solvers.SolverFactory("glpk")

model = ConcreteModel()

model.x = Var(within=NonNegativeReals)
model.y = Var(within=NonNegativeReals)

model.c1 = Constraint(expr = model.x + 3*model.y <= 8)
model.c2 = Constraint(expr = model.x + model.y <= 4)
model.z = Objective(expr = model.x + 2*model.y, sense=maximize)
results = opt.solve(model)
model.pprint()
#print values
print("solutions:  ")
print(f"x value: {model.x.get_values()[None]}")
print(f"y value: {model.y.get_values()[None]}")
# I'll copy paste the output here:
'''
2 Var Declarations
    x : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   2.0 :  None : False : False : NonNegativeReals
    y : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   2.0 :  None : False : False : NonNegativeReals

1 Objective Declarations
    z : Size=1, Index=None, Active=True
        Key  : Active : Sense    : Expression
        None :   True : maximize : x + 2*y

2 Constraint Declarations
    c1 : Size=1, Index=None, Active=True
        Key  : Lower : Body    : Upper : Active
        None :  -Inf : x + 3*y :   8.0 :   True
    c2 : Size=1, Index=None, Active=True
        Key  : Lower : Body  : Upper : Active
        None :  -Inf : x + y :   4.0 :   True

5 Declarations: x y c1 c2 z
solutions:  
x value: 2.0
y value: 2.0
'''
