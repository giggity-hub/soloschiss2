import argparse
import json
import os
import sys
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import wordpunct_tokenize as tokenizer

root_dir = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(root_dir)
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
    bleu_scores = []

    for dialogue in data:
        # get reply for calculating BLEU
        reply_gold = dialogue['reply_gold'].replace('system :', '', 1).strip()
        reply_pred = dialogue['reply_pred'].replace('system :', '', 1).strip()
        bleu_scores.append(sentence_bleu([tokenizer(reply_gold)], tokenizer(reply_pred)))

        # get belief for calculating accuracy/precision/recall
        belief_gold = parse_beliefstate(dialogue['belief_gold'].replace('belief :', '', 1).strip())
        belief_pred = parse_beliefstate(dialogue['belief_pred'].replace('belief :', '', 1).strip())

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

    bleu = sum(bleu_scores) / len(bleu_scores)
    accuracy = full_matches / total_dialogues
    precision = tp_attr / (tp_attr + fp_attr) if (tp_attr + fp_attr) > 0 else 0
    recall = tp_attr / (tp_attr + fn_attr) if (tp_attr + fn_attr) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f'Total dialogues: {total_dialogues}')
    print(f'Accuracy (exact matches): {accuracy:.2f}')
    print(f'Macro-averaged BLEU score: {bleu:.2f}')
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
