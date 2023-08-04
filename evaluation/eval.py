import argparse
import json
import os
import sys
import warnings
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import wordpunct_tokenize as tokenizer

root_dir = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(root_dir)
from stuttbard.chatbot.evaluate import parse_beliefstate, find_all_slots_in_template


def calculate_prf(tp: int, fp: int, fn: int) -> (float, float, float):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0
    f = 2 * (p * r) / (p + r) if (p + r) > 0 else 0
    return p, r, f


def main(test_file: str, verbose: bool = False):
    with open(test_file, 'r') as f:
        data = json.load(f)

    total_dialogues = len(data)

    # confusion matrix for belief state
    total_attr = 0
    full_belief = 0
    tp_attr = 0  # attributes that are both in gold and predicted
    fp_attr = 0  # attributes in predicted but not in gold
    fn_attr = 0  # in gold but not in predicted

    # confusion matrix for response template
    total_slot = 0
    full_template = 0
    tp_slot = 0
    fp_slot = 0
    fn_slot = 0

    bleu_scores = []

    for dialogue in data:
        # clean up the system response, only leave the actual response string
        reply_gold = dialogue['reply_gold'].replace('system :', '', 1).strip()
        reply_pred = dialogue['reply_pred'].replace('system :', '', 1).strip()

        # calculate BLEU
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            bleu_scores.append(sentence_bleu([tokenizer(reply_gold)], tokenizer(reply_pred)))

        # get template slots
        slots_gold = set([x for x in find_all_slots_in_template(reply_gold) if x != 'slot_entity_name'])
        slots_pred = set([x for x in find_all_slots_in_template(reply_pred) if x != 'slot_entity_name'])

        total_slot += len(slots_gold)

        if slots_gold == slots_pred:
            full_template += 1
            tp_slot += len(slots_gold)
        else:
            tp_slot += len(slots_gold.intersection(slots_pred))
            fn_slot += len(slots_gold - slots_pred)
            fp_slot += len(slots_pred - slots_gold)

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
            full_belief += 1
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
    acc_belief = full_belief / total_dialogues
    acc_template = full_template / total_dialogues
    p_belief, r_belief, f1_belief = calculate_prf(tp_attr, fp_attr, fn_attr)
    p_template, r_template, f1_template = calculate_prf(tp_slot, fp_slot, fn_slot)

    print(f'Total dialogues: {total_dialogues}')
    print(f'Macro-averaged BLEU score: {bleu:.2f}')

    print('\nAccuracy (exact matches)')
    print(f'Belief: {acc_belief:.2f}')
    print(f'Template: {acc_template:.2f}')

    print('\nAttribute-level metrics (belief state)')
    print(f'Precision: {p_belief:.2f}')
    print(f'Recall: {r_belief:.2f}')
    print(f'F1 score: {f1_belief:.2f}')

    print('\nSlot-level metrics (template)')
    print(f'Precision: {p_template:.2f}')
    print(f'Recall: {r_template:.2f}')
    print(f'F1 score: {f1_template:.2f}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='Path to the JSON test file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Display the evaluation of every dialogue')
    args = parser.parse_args()

    main(args.test_file, args.verbose)
