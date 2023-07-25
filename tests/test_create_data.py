from domains.domains import load_domain_sampler
from domains.domains import domains_dict
from scripts.create_data import parametrize, _parametrize
from scripts.create_data import get_samples
from utils.unique_random import UniqueRandom

sampler = load_domain_sampler(domains_dict)


def test_get_samples():
    sampler = UniqueRandom([('World', 1)])
    samplers_dict = {
        "first_param, second_param": sampler
    }

    format_dict = get_samples(samplers_dict)
    print(format_dict)

    assert format_dict["first_param"] == 'World'
    assert format_dict["second_param"] == 1


def test__parametrize():
    sampler = UniqueRandom([('World', 1)])
    results = _parametrize({
        "samplers": {"first_param, second_param": sampler},
        "belief": "Goodbye %(first_param)s %(second_param)s",
        "user_system": [
            ("Hello", "Hello %(first_param)s %(second_param)s")
        ]
    })

    response = results[0]

    assert response['belief'] == "Goodbye World 1"
    assert response['system'] == "Hello World 1"

def test_parametrize():
    config = {
        "samplers": {'about': lambda s : s['museum']['about']},
        "belief": "",
        "user_system": [
            ("i want to see a museum about %(about)s", "here is a museum about %(about)s"),
            ("i want to see a museum about %(about)s", "here is a museum about %(about)s")
        ]
    }

    train_moped, test_mopeds = parametrize(config)
    print(train_moped)
    print(test_mopeds)