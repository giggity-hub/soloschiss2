import json
from sql_training_data.data import data

def to_soloist_format(interaction):
    history = []
    res = []
    for time_point in interaction:
        history.append(f'user : {time_point["user"]}')
        reply = f"system : {time_point['system']}"
        belief = f"belief : {time_point['belief']}"
        
        res.append({
            "history": [*history],
            "belief": belief,
            "reply": reply,
            "kb": ""
        })
        history.append(reply)

    return res

soloist_data = []
for history in data:
    soloist_data += to_soloist_format(history)

with open('kb.soloist.json', 'w') as f:
    json.dump(soloist_data, f, indent=4)