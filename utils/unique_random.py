import random
import numpy as np

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
        
def get_sampler_split(list_to_split : list, split_fraction : float):
    
    split_idx = int(np.round(len(list_to_split) * split_fraction))
    #print("split_idx:", split_idx)
    split_A = list_to_split[:split_idx]
    split_B = list_to_split[split_idx:]
    #print("len A:", len(split_A))
    #print("len B:", len(split_B))
    #print(split_A)
    #print(split_B)
    return UniqueRandom(split_A), UniqueRandom(split_B)
    
#samplerA, samplerB = get_sampler_split(list(range(10)), 0.55)


