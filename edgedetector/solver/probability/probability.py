class Probability:

    def __init__(self, base_crossover_prob, base_mutation_prob):
        self.mutation_probability = base_mutation_prob
        self.crossover_probability = base_crossover_prob

    def update(self):
        None


class IntelligentProbability(Probability):
    def __init__(self, base_crossover_prob, base_mutation_prob,
                 steps_duration=5, crossover_change_rate = 0.9, mutation_change_rate = 5):
        super().__init__(base_crossover_prob, base_mutation_prob)
        self.steps_duration = steps_duration
        self.crossover_change_rate = crossover_change_rate
        self.mutation_change_rate = mutation_change_rate
        self.steps_from_update = 0

    def update(self):
        self.steps_from_update += 1
        if self.steps_from_update == self.steps_duration:
            self.steps_from_update = 0
            self.crossover_probability *= self.crossover_change_rate
            self.mutation_probability *= self.mutation_change_rate
            print("values changed mutation = ", self.mutation_probability, ", crossover = ", self.crossover_probability)
