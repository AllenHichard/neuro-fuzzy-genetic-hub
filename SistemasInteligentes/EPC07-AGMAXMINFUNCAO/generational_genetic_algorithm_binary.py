from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import BitFlipMutation, SPXCrossover, BinaryTournamentSelection
from problem_max_point import OneMaxPoint
from jmetal.util.termination_criterion import StoppingByEvaluations

def generational_binary(populacao_tam, geracao_qtd, cruzamento, mutacao, taxaElitismo):
    problem = OneMaxPoint(number_of_bits=22)

    algorithm = GeneticAlgorithm(
        problem=problem,
        population_size=populacao_tam,
        offspring_population_size=100,
        mutation=BitFlipMutation(mutacao),
        crossover=SPXCrossover(cruzamento),
        selection=BinaryTournamentSelection(),
        termination_criterion=StoppingByEvaluations(max_evaluations=populacao_tam*geracao_qtd)
    )

    algorithm.run()
    result = algorithm.get_result()

    print('Algorithm: {}'.format(algorithm.get_name()))
    print('Problem: {}'.format(problem.get_name()))
    print('best_id: ' + str(problem.idbest_individuo))
    print('max: ' + str(problem.idIndividuo))
    print('Solution: ' + result.get_binary_string())
    print('Fitness:  ' + str(-result.objectives[0]))
    print('Computing time: {}'.format(algorithm.total_computing_time))
    return problem.geracoes, problem.melhoresX, problem.melhoresY
