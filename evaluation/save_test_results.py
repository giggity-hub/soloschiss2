"""
Based on json test data, saves the output of the model in a file.
The output file is saved in the same directory as the test file

Output format:
[
    {
        "history": [
            "user : user input"
        ],
        "kb": "",
        "belief_gold": "belief : gold belief state",
        "belief_pred": "belief : predicted belief state",
        "reply_gold": "system : gold system reply",
        "reply_pred": "system : predicted system reply"
    },
]
"""
import argparse
import json
import os
import sys
from tqdm import tqdm

root_dir = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(root_dir)
from stuttbard.chatbot.chat import query_soloist


def main(test_file: str):
    with open(test_file, 'r') as f:
        data = json.load(f)

    results = []

    for dialogue in tqdm(data):
        out = dict()

        user_inp = dialogue['history']

        raw_output = query_soloist(user_inp)

        split_at = raw_output.find('system : ')
        system_response = raw_output[split_at:].strip()
        belief_string = raw_output[:split_at].strip()

        out['history'] = dialogue['history']
        out['kb'] = dialogue['kb']
        out['belief_gold'] = dialogue['belief']
        out['belief_pred'] = f'belief : {belief_string}'
        out['reply_gold'] = dialogue['reply']
        out['reply_pred'] = system_response

        results.append(out)

    with open(f'{test_file.replace(".json", "", 1)}_out.json', 'w') as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to the JSON test file')
    args = parser.parse_args()
    main(args.test_file)
