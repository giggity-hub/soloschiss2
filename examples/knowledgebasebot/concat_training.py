"""
Concatenate all files in the training_data directory into a single JSON file
"""
import os
import json

directory = 'training_data'

concat_data = []

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(os.path.join(directory, filename), 'r') as f:
            contents = json.load(f)
            concat_data += contents

out = 'kb.soloist.json'
with open(out, 'w') as file:
    json.dump(concat_data, file, indent=4)
