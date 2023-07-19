import random

class UniqueRandom:
    def __init__(self, options) -> None:
        # Make sure there are no duplicates in the list
        self.options = list(set(options))
        random.shuffle(self.options)
        self.index = 0
        self.max_index = len(options) -1
    
    def sample(self):
        if self.index >= self.max_index:
            random.shuffle(self.options)
            self.index = 0
        
        value = self.options[self.index]
        self.index += 1
        return value