from Individual import Individual
import

POPULATION_SIZE = 50


class Population:

    def __init__(self):
        self.individuals = []
        for x in range(POPULATION_SIZE):
            self.individuals.append(Individual(60))

    def simulate(self):
        return 0

    def fitness(self):
        return 0

