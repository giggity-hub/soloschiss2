"""
Converts CSV file with multiturn dialogues to Soloist training data format
"""
import csv
import json
from copy import deepcopy


with open('training_data/multiturn.csv', 'r', encoding='utf-8-sig') as f:
    csv_reader = csv.reader(f, delimiter=',' )
    converted_data = []
    current_turn = None

    for row in csv_reader:
        turn_id = int(row[0])
        message = row[1]
        belief = row[2]

        # create a new dialogue
        if turn_id == 0:
            current_turn = {
                "history": [],
                "belief": "",
                "kb": "",
                "reply": ""
            }

        # user turn
        if turn_id % 2 == 0:
            current_turn["history"].append(f"user : {message}")
            # belief is only updated on user turns
            current_turn["belief"] = f"belief : {belief}"
        # system turn
        else:
            current_turn["reply"] = f"system : {message}"
            converted_data.append(deepcopy(current_turn))
            # update the history with system message
            current_turn["history"].append(f"system : {message}")

with open('training_data/multiturn.json', 'w') as out:
    json.dump(converted_data, out, indent=4)
