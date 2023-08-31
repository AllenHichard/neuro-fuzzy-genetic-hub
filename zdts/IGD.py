import numpy
from pymoo.factory import get_performance_indicator
from pymoo.factory import get_problem

def arquivo_to_list(fronteira):
    lista = []
    for linha in fronteira:
        linha = linha.replace("\n","").replace("\t"," ")
        valores = linha.split(" ")
        param1 = float(valores[0])
        param2 = float(valores[1])
        ponto = [param1, param2]
        lista.append(ponto)
    return numpy.array(lista)

def IGD(problem, fronteira_problema, fronteira_ag):
    # The pareto front of a scaled zdt1 problem
    pf = arquivo_to_list(fronteira_problema)
    # The result found by an algorithm
    A = arquivo_to_list(fronteira_ag)
    # plot the result

    igd = get_performance_indicator("igd", pf)
    print(problem, "IGD", igd.calc(A))


fronteira_problema = open(".\\resultado\\fronteira_problema\\ZDT1.pf", "r")
fronteira_ag = open(".\\resultado\\FUN.NSGAII.ZDT1")

IGD("ZDT1", fronteira_problema, fronteira_ag)

fronteira_problema = open(".\\resultado\\fronteira_problema\\ZDT2.pf", "r")
fronteira_ag = open(".\\resultado\\FUN.NSGAII.ZDT2")
IGD("ZDT2", fronteira_problema, fronteira_ag)

fronteira_problema = open(".\\resultado\\fronteira_problema\\ZDT3.pf", "r")
fronteira_ag = open(".\\resultado\\FUN.NSGAII.ZDT3")
IGD("ZDT3", fronteira_problema, fronteira_ag)

