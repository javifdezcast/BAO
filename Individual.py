import random
import main
from PlayerCar import PlayerCar
from vector2 import Vector2


class Individual:
    def __init__(self, simulation_time, time_step):
        steps = int(simulation_time / time_step)
        self.gen = []
        # self.position = Vector2()
        # self.direction = Vector2()
        self.car = PlayerCar(4,4)
        for x in range(steps):
            self.gen.append((self.random_value(1), self.random_value(1)))

    def random_value(self, k):
        num = random.random()
        if num < 0.2:
            return 0
        elif num < 0.6:
            return-1
        else:
            return 1

    # def print_individual(self):
    #     print(f"{self.position}", end=' ')
    #     print(f"{self.direction} genome = {self.gen}", end=' ')

    def simulate(self, genoma):
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
        for g in genoma:
            main.move_player(self.car, g[0], g[1])
            main.handle_collision(self.car)
        check_x = self.car.distance_next_checkpoint(main.CHECKPOINT_OBJECTS[self.car.next_checkpoint()].centre_x)
        check_y = self.car.distance_next_checkpoint(main.CHECKPOINT_OBJECTS[self.car.next_checkpoint()].centre_y)
        return self.car.next_checkpoint(), self.car.distance_next_checkpoint(check_x, check_y), self.car.crashes

    def reward(self, genoma):
        values = self.simulate(genoma)
        return 100 * values[0] + values[1] - 10 * values[2]
#
# sim_time = 3
# sim_step = 1
# population_size = 1
#
# population = []
# for i in range(population_size):
#     population.append(Individual(Vector2(), Vector2(1.0, 0.0), sim_time, sim_step))
#
# for i in population:
#     i.print_individual()
# print()
# print()
#
# for i in population:
#     positions = i.simulate()
#     print()
#     for j in positions:
#         print(i.position)
#
