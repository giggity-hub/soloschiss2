from utils.unique_random import UniqueRandom

def test_unique_random():
    sampler = UniqueRandom([('yeah boi', 1)])
    sample_first, sample_second = sampler.sample()
    assert sample_first == 'yeah boi'
    assert sample_second == 1


    