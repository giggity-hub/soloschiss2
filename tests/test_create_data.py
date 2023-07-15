from stuttbard.domains.sampler import create_sampler
from stuttbard.scripts.create_data import parametrize
from stuttbard.scripts.create_data import get_samples
from stuttbard.domains.sampler import UniqueRandom

def test_unique_random():
    sampler = UniqueRandom([('yeah boi', 1)])
    sample_first, sample_second = sampler.sample()
    assert sample_first == 'yeah boi'
    assert sample_second == 1

def test_create_sampler():
    sampler = create_sampler()

sampler = create_sampler()

def test_sampler_index():
    index_str, index_int = sampler['index'].sample()
    assert type(index_str) == str
    assert len(index_str) > 0
    assert type(index_int) == int


def test_get_samples():
    sampler = UniqueRandom([('World', 1)])
    samplers_dict = {
        "first_param, second_param": sampler
    }

    format_dict = get_samples(samplers_dict)

    assert format_dict["first_param"] == 'World'
    assert format_dict["second_param"] == 1


def test_parametrize():
    sampler = UniqueRandom([('World', 1)])
    results = parametrize({
        "samplers": {"first_param, second_param": sampler},
        "belief": "Goodbye %(first_param)s %(second_param)s",
        "user_system": [
            ("Hello", "Hello %(first_param)s %(second_param)s")
        ]
    })

    response = results[0]

    assert response['belief'] == "Goodbye World 1"
    assert response['system'] == "Hello World 1"