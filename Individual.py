import random
import main.py
from vector2 import Vector2
from PIL import Image


class Individual:
    def __init__(self, position, direction, simulation_time, time_step):
        steps = int(simulation_time / time_step)
        self.gen = []
        self.position = Vector2()
        self.direction = Vector2()
        self.car = PlayerCar(4,4)
        self.crashes = 0
        self.checkpoints = 0
        for x in range(steps):
            self.gen.append((self.random_value(1), self.random_value(1)))

    def random_value(self, k):
        return (random.random() - 0.5) * k if random.random() > 0.0 else 0.0

    def print_individual(self):
        print(f"{self.position}", end=' ')
        print(f"{self.direction} genome = {self.gen}", end=' ')

    def simulate(self):
        # self.direction.normalize()
        # positions = []
        # velocity = Vector2()
        # for g in self.gen:
        #     print("directionbefore", self.direction)
        #     self.direction.rotate(g[0])
        #     print("directionafter", self.direction)
        #
        #     velocity += g[0] * self.direction
        #     self.position += g[1] * velocity
        #     pos = self.position
        #     positions.append( pos )
        # return positions
        positions = []
        for g in self.gen:
            main.move_player(self.car, gen[0], gen[1])
            reward = main.handle_collision(self.car)
            positions.append( self.car.x, self.car.y)
        return positions


sim_time = 3
sim_step = 1
population_size = 1

population = []
for i in range(population_size):
    population.append(individual(Vector2(), Vector2(1.0, 0.0), sim_time, sim_step))

for i in population:
    i.print_individual()
print()
print()

for i in population:
    positions = i.simulate()
    print()
    for j in positions:
        print(i.position)

