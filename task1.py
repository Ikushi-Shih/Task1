import random
class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = [-1, 0, 1, 2, 3]
    # Probability of the occurence of random_nums
    _probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    def next_num(self):
        return random.choices(self._random_nums, self._probabilities)
        pass
    
RandomGen().next_num()

