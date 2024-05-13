from random import Random
from time import time

import main
from Individual import Individual
from inspyred import ec, benchmarks

POPULATION_SIZE = 50


class Evolutionary(benchmarks.Benchmark):

    bounder = None
    maximize = None

    def __init__(self):
        benchmarks.Benchmark.__init__(self, 0)
        self.bounder = ec.DiscreteBounder([0, 1])
        self.maximize = True
        self.generacion = 0

    def generator(self, random, args):
        individual = Individual(60, 1 / 60)
        return individual.gen

    def evaluator(self, candidates, args):
        s = "generacion "
        print(s, self.generacion, sep='')
        fitness = []
        c = 0
        for candidate in candidates:
            b = "    individuo "
            print(b, c, sep='')
            c=c+1
            a = main.main()
            num = a.simulate(candidate)
            fitness.append(num)
        self.generacion=self.generacion+1
        return fitness


seed = time()
prng = Random()
prng.seed(seed)

evolutionary = Evolutionary()

ga = ec.GA(prng)
ga.selector = ec.selectors.fitness_proportionate_selection
ga.variator = [ec.variators.n_point_crossover, ec.variators.bit_flip_mutation]
ga.replacer = ec.replacers.generational_replacement
ga.terminator = ec.terminators.generation_termination
final_pop = ga.evolve(generator=evolutionary.generator,
                      evaluator=evolutionary.evaluator,
                      bounder=evolutionary.bounder,
                      maximize=evolutionary.maximize,
                      pop_size=2,
                      max_generations=3,
                      num_elites=1,
                      num_selected=3,
                      crossover_rate=1,
                      num_crossover_points=1,
                      mutation_rate=0.05)

best = max(ga.population)
print('Best Solution: {0}: {1}'.format(str(best.candidate), best.fitness))

pantalla = main.main()
pantalla.view_solution(best.candidate)
