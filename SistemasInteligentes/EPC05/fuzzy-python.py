import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temperatura = ctrl.Antecedent(np.arange(800, 1201, 1/500), 'temperatura')
volume = ctrl.Antecedent(np.arange(2.0, 12.1, 1/500), 'volume')
pressao = ctrl.Consequent(np.arange(4, 13, 1/500), 'pressao')


temperatura['low'] = fuzz.trapmf(temperatura.universe, [800, 800, 900, 1000])
temperatura['medium'] = fuzz.trimf(temperatura.universe, [900, 1000, 1100])
temperatura['high'] = fuzz.trapmf(temperatura.universe, [1000, 1100, 1200, 1200])

volume['small'] = fuzz.trapmf(volume.universe, [2.0, 2.0, 4.5, 7.0])
volume['medium'] = fuzz.trimf(volume.universe, [4.5, 7.0, 9.5])
volume['big'] = fuzz.trapmf(volume.universe, [7.0, 9.5, 12.0, 12.0])

pressao['low'] = fuzz.trapmf(pressao.universe, [4, 4, 5, 8])
pressao['medium'] = fuzz.trimf(pressao.universe, [6, 8, 10])
pressao['high'] = fuzz.trapmf(pressao.universe, [8, 11, 12, 12])

#maxmin composition


regra1 = ctrl.Rule(temperatura['low'] & volume['small'], pressao['low'])
regra2 = ctrl.Rule(temperatura['medium'] & volume['small'], pressao['low'])
regra3 = ctrl.Rule(temperatura['high'] & volume['small'], pressao['medium'])

regra4 = ctrl.Rule(temperatura['low'] & volume['medium'], pressao['low'])
regra5 = ctrl.Rule(temperatura['medium'] & volume['medium'], pressao['medium'])
regra6 = ctrl.Rule(temperatura['high'] & volume['medium'], pressao['high'])

regra7 = ctrl.Rule(temperatura['low'] & volume['big'], pressao['medium'])
regra8 = ctrl.Rule(temperatura['medium'] & volume['big'], pressao['high'])
regra9 = ctrl.Rule(temperatura['high'] & volume['big'], pressao['high'])


sistema = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
simulation = ctrl.ControlSystemSimulation(sistema)

temperaturas = [965, 920, 1050, 843, 1122]
pressao = [11, 7.6, 6.3, 8.6, 5.2]

for temp, pres in zip(temperaturas, pressao):
    simulation.input['temperatura'] = temp
    simulation.input['volume'] = pres
    simulation.compute()
    print(simulation.output['pressao'])


#print(temperatura.view())
#temperatura.view()
#
#volume.view()
#pressao.view()
#plt.show()

