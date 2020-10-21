import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# New Antecedent/Consequent objects hold universe variables and membership
# functions
'''
cromo = ["low", "small", "low", "small", "low", "small", "low","small", "low","small", "low","small", "low","small", "low","small", "low","small", "low","small",
         "low","small", "low","small", "low","small", "low","small", "low","small", "low", 1000, 7.0, 8]


entrada = 3
lista = []

for e in range(entrada):
    data = dataset1
    lista.append(ctrl.Antecedent(np.arange(data[e][0], data[1], 1), 'temperatura'))
'''
cromo = [1000, 7.0, 8]
temperatura = ctrl.Antecedent(np.arange(800, 1201, 1), 'temperatura')
volume = ctrl.Antecedent(np.arange(2.0, 12.1, 0.5), 'volume')
pressao = ctrl.Consequent(np.arange(4, 13, 1), 'pressao')
# Auto-membership function population is possible with .automf(3, 5, or 7)

temperatura['low'] = fuzz.trapmf(temperatura.universe, [800, 800, 900, cromo[0]])
temperatura['medium'] = fuzz.trimf(temperatura.universe, [900, cromo[0], 1100])
temperatura['high'] = fuzz.trapmf(temperatura.universe, [cromo[0], 1100, 1200, 1200])

volume['small'] = fuzz.trapmf(volume.universe, [2.0, 2.0, 4.5, cromo[1]])
volume['medium'] = fuzz.trimf(volume.universe, [4.5, cromo[1], 9.5])
volume['big'] = fuzz.trapmf(volume.universe, [cromo[1], 9.5, 12.0, 12.0])

pressao['low'] = fuzz.trapmf(pressao.universe, [4, 4, 5, cromo[2]])
pressao['medium'] = fuzz.trimf(pressao.universe, [6, cromo[2], 10])
pressao['high'] = fuzz.trapmf(pressao.universe, [cromo[2], 11, 12, 12])

regra1 = ctrl.Rule(temperatura['low'] & volume['small'], pressao['low'])
regra2 = ctrl.Rule(temperatura['medium'] & volume['small'], pressao['low'])
regra3 = ctrl.Rule(temperatura['high'] & volume['small'], pressao['medium'])

regra4 = ctrl.Rule(temperatura['low'] & volume['medium'], pressao['low'])
regra5 = ctrl.Rule(temperatura['medium'] & volume['medium'], pressao['medium'])
regra6 = ctrl.Rule(temperatura['high'] & volume['medium'], pressao['high'])

regra7 = ctrl.Rule(temperatura['low'] & volume['big'], pressao['medium'])
regra8 = ctrl.Rule(temperatura['medium'] & volume['big'], pressao['high'])
regra9 = ctrl.Rule(temperatura['high'] & volume['big'], pressao['high'])

sist = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
test_sist = ctrl.ControlSystemSimulation(sist)

test_sist.input['temperatura'] = 965
test_sist.input['volume'] = 11
test_sist.compute()
test_sist.print_state()
print(test_sist.output['pressao'])
temperatura.view(sim=test_sist)
volume.view(sim=test_sist)
pressao.view(sim=test_sist)


plt.show()