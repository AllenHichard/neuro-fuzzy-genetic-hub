#https://pymoo.org/misc/performance_indicator.html
from pymoo.factory import get_performance_indicator
fronteira_problema = open(".\\resultado\\fronteira_problema\\ZDT2.pf", "r")
fronteira_ag = open(".\\resultado\\FUN.NSGAII.ZDT2")

#print(len(fronteira_problema.read()))
#print(len(fronteira_ag.read()))

import numpy as np
from pymoo.factory import get_problem
from pymoo.visualization.scatter import Scatter

# The pareto front of a scaled zdt1 problem
pf = get_problem("zdt1").pareto_front()
print(len(pf), pf, type(pf))
# The result found by an algorithm
A = pf[::10] * 1.1
print(len(A))
# plot the result
#Scatter(legend=True).add(pf, label="Pareto-front").add(A, label="Result").show()
igd = get_performance_indicator("igd", pf)
print("IGD", igd.calc(A))