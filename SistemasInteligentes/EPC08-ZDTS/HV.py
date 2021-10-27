import numpy
from pymoo.factory import get_performance_indicator
from pymoo.factory import get_problem

#quanto maior o valor de HV melhores são resultados. https://pymoo.org/misc/performance_indicator.html
"""
Esta imagem foi tirada de [25] e ilustra um exemplo de dois objetivos onde a área que é dominada 
por um conjunto de pontos é mostrada em cinza. Considerando que para as outras métricas, o objetivo 
era minimizar a distância para a frente de Pareto, aqui, desejamos maximizar a métrica de desempenho.
"""
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

def HV(problem, fronteira_problema, fronteira_ag, pontoReferencia):
    # The pareto front of a scaled zdt1 problem
    pf = arquivo_to_list(fronteira_problema)
    # The result found by an algorithm
    A = arquivo_to_list(fronteira_ag)
    # plot the result

    hv = get_performance_indicator("hv", ref_point=numpy.array(pontoReferencia))
    print(problem, "HV", hv.calc(A))


fronteira_problema = open(".\\resultado\\fronteira_problema\\ZDT1.pf", "r")
fronteira_ag = open(".\\resultado\\FUN.NSGAII.ZDT1")
HV("ZDT1", fronteira_problema, fronteira_ag, [1.0, 1.0])

fronteira_problema = open(".\\resultado\\fronteira_problema\\ZDT2.pf", "r")
fronteira_ag = open(".\\resultado\\FUN.NSGAII.ZDT2")
HV("ZDT2", fronteira_problema, fronteira_ag, [1.0, 1.0])

fronteira_problema = open(".\\resultado\\fronteira_problema\\ZDT3.pf", "r")
fronteira_ag = open(".\\resultado\\FUN.NSGAII.ZDT3")
HV("ZDT3", fronteira_problema, fronteira_ag, [1.0, 1.0])



"""
O ponto de referência pode ser definido construindo-se um vetor com os piores valores
de função objetivo. Esse ponto é apenas uma referência para o cálculo do volume em relação
ao Pareto Front, sendo normalmente representado por um ponto onde contém os piores
valores das funções objetivo.

ref: https://repositorio.ufpe.br/bitstream/123456789/12400/1/Disserta%C3%A7ao%20Leonardo%20Nunes.pdf
"""