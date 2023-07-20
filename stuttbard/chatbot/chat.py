import re
from domains.domains import domains_dict
from argparse import Namespace
import requests
from stuttbard.chatbot.evaluate import evaluate

def query_soloist(history):
    r = requests.get('http://localhost:8000', json={'history': history})
    return r.text


def start():
    domains = domains_dict
    df = None
    entity = None
    
    while True:
        # Get Model Output for User Input
        user_in = input()
        user_in_prefixed = f'user : {user_in}'
        # history.append(user_in_prefixed)

        raw_output = query_soloist([user_in_prefixed])

        split_at = raw_output.find('system : ')
        system_response = raw_output[split_at:]
        belief_string = raw_output[:split_at]

        sample = {
            'belief': belief_string,
            'system': system_response
        }

        res = "I sorry i did not understand that"
        print(f"raw model output: {raw_output}")
        print(f"sample: {sample}")
        try:
            res, df, entity = evaluate(sample, domains, df, entity)
        except Exception as e:
            print(e)
            
        # print(domains['restaurant'])
        # self.history.append(system_response)

        print(f"res: {res}")


if __name__ == "__main__":
    start()
    # print(domains)
    # print("sheeeeeeesh")

    # print(df)
    # chat = Chat()
    # chat.start()