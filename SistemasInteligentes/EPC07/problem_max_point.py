import math
import random

from jmetal.core.problem import BinaryProblem, FloatProblem
from jmetal.core.solution import BinarySolution, FloatSolution

"""
.. module:: unconstrained
   :platform: Unix, Windows
   :synopsis: Unconstrained test problems for single-objective optimization

.. moduleauthor:: Antonio J. Nebro <antonio@lcc.uma.es>, Antonio Benítez-Hidalgo <antonio.b@uma.es>
"""

class OneMaxPoint(BinaryProblem):

    def __init__(self, number_of_bits: int = 256):
        super(OneMaxPoint, self).__init__()
        self.geracoes = []
        self.melhoresX = []
        self.melhoresY = []
        self.idIndividuo = 0
        self.idbest_individuo = 0
        self.number_of_bits = number_of_bits
        self.number_of_objectives = 1
        self.number_of_variables = 1
        self.number_of_constraints = 0
        self.bestx = -2
        self.besty = -2
        self.obj_directions = [self.MAXIMIZE]
        self.obj_labels = ['Ones']

    def evaluate(self, solution: BinarySolution) -> BinarySolution:
        binario = ""
        self.idIndividuo+=1
        #print(solution.variables[0])
        for bits in solution.variables[0]:
            if bits:
                binario += "1"
            else:
                binario += "0"
        convertido = int(binario, 2)
        x = -1.0 + convertido*(3/((2**22)-1)) # intervalo
        y = x*math.sin(10*math.pi*x) + 1
        if self.besty < y:
            self.besty = y
            self.bestx = x
            self.idbest_individuo = self.idIndividuo
            self.geracoes.append(int(self.idbest_individuo/200) + 1)
            self.melhoresX.append(x)
            self.melhoresY.append(y)
            #print("x", x, "y", y)
        solution.objectives[0] = round(-y, 6)
        return solution

    def create_solution(self) -> BinarySolution:
        new_solution = BinarySolution(number_of_variables=1, number_of_objectives=1)
        new_solution.variables[0] = \
            [True if random.randint(0, 1) == 0 else False for _ in range(self.number_of_bits)]
        return new_solution

    def get_name(self) -> str:
        return 'OneMaxPoint'

