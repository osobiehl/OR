#following Petrat
from pyomo.environ import *
from pyomo.opt import *
import pprint
opt = solvers.SolverFactory("glpk")

model = ConcreteModel()
BIGNUM = 2**40

To = ['Dortmund', 'Osnabruck', 'Bremerhaven']
From = ['Hamburg', 'Hannover', 'Bremen']

w={ ('Hamburg', 'Dortmund'): 36, ('Hamburg', 'Osnabruck'): 45, ('Hamburg', 'Bremerhaven'): 65,
    ('Hannover', 'Dortmund'):35, ('Hannover', 'Osnabruck'):20, ('Hannover', 'Bremerhaven'): 35,
    ('Bremen', 'Dortmund'): 60,  ('Bremen', 'Osnabruck'): 30 , ('Bremen', 'Bremerhaven'): 19
    
}
# print(w)# constraint matrix
d = { 'Dortmund':25, 'Osnabruck': 12, 'Bremerhaven': 7} #demand constraints

s = {'Hamburg':20,'Hannover':14,'Bremen':11} # production constraints

def demand_rule(model, j):
    return sum(model.x[i,j] for i in From ) == d[j]

def supply_rule(model, i):
    return sum(model.x[i,j] for j in To) <= s[i]


model.x = Var(From, To, within=NonNegativeReals)

model.z = Objective(expr=sum( (    w[i,j] * model.x[i,j] ) for j in To for i in From), sense=minimize)
#set constraints
model.supply = Constraint(From, rule=supply_rule)
model.demand=Constraint(To, rule=demand_rule)



# model.dual = Suffix(direction=Suffix.IMPORT)
results = opt.solve(model)
# model.pprint()

# print(model.x.get_values())
pprint.pprint(model.x.get_values())
print(f"total cost of transportation: {model.z.expr()}")
