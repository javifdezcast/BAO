import random

class individual:

    def __init__(self, sec):
        self.genoma = []
        for x in range(sec*60):
            self.genoma.append([self.randomValue(1), self.randomValue(1)])

    def random_value(self, k):
        if random.random() < 0.5:
            return 0.0
        return (random.random() - 0.5) * k
