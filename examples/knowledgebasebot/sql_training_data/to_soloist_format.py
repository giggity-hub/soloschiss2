prefix_system = lambda x : 'system : ' + x
prefix_user = lambda x : 'user : ' + x
prefix_belief = lambda x : 'belief : ' + x


def to_soloist_format(compact_dict):
    soloist_dict = {
        "history": [prefix_user(compact_dict['user'])],
        "belief": prefix_belief(compact_dict["belief"]),
        "kb": "",
        "reply": prefix_system(compact_dict["system"])
    }
    return soloist_dict