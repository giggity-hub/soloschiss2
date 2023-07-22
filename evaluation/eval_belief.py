import argparse
import json
import os
import sys

root_dir = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(root_dir)
from stuttbard.chatbot.chat import query_soloist
from stuttbard.chatbot.evaluate import parse_beliefstate


def main(test_file: str, verbose: bool = False):
    with open(test_file, 'r') as f:
        data = json.load(f)

    total_dialogues = len(data)
    full_matches = 0
    total_attr = 0
    tp_attr = 0  # attributes that are both in gold and predicted
    fp_attr = 0  # attributes in predicted but not in gold
    fn_attr = 0  # in gold but not in predicted

    for dialogue in data:
        user_inp = dialogue['history']
        raw_output = query_soloist(user_inp)

        belief_string = dialogue['belief'][9:]
        belief_gold = parse_beliefstate(belief_string)

        split_at = raw_output.find('system : ')
        belief_pred = parse_beliefstate(raw_output[:split_at])

        total_attr += len(belief_gold)

        if verbose:
            print(f'gold: {belief_gold}')
            print(f'pred: {belief_pred}')

        # check for a full match
        if belief_gold == belief_pred:
            if verbose:
                print('Full match!\n')
            full_matches += 1
            tp_attr += len(belief_gold)
            continue

        gold_items = set(belief_gold.items())
        pred_items = set(belief_pred.items())

        tp = len(gold_items.intersection(pred_items))
        fn = len(gold_items - pred_items)
        fp = len(pred_items - gold_items)

        if verbose:
            print(f'TP {tp}\tFN {fn}\tFP {fp}\n')

        tp_attr += tp
        fn_attr += fn
        fp_attr += fp

    accuracy = full_matches / total_dialogues
    precision = tp_attr / (tp_attr + fp_attr) if (tp_attr + fp_attr) > 0 else 0
    recall = tp_attr / (tp_attr + fn_attr) if (tp_attr + fn_attr) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f'Total dialogues: {total_dialogues}')
    print(f'Accuracy (exact matches): {accuracy:.2f}')
    print('\nAttribute-level metrics')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1 score: {f1:.2f}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to the JSON test file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Display the evaluation of every dialogue')
    args = parser.parse_args()

    main(args.test_file, args.verbose)
