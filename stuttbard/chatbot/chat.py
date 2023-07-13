import pandas as pd
from selection import Selection
# from actions import Actions
from soloist_parser import parse_soloist_output
import re


def find_action(self, string):
    action_regexp = 'action_[a-z_]+'
    found_actions = re.findall(action_regexp, string)

    print(f'found actions {found_actions}')
    if len(found_actions) == 0:
        return None
    
    action_name = found_actions[0].replace('action_', '')
    return action_name




def load_knowledgebase_df():
    kb_df = pd.read_csv('data.csv')
    # make entire dataset lowercase
    kb_df = kb_df.apply(lambda x: x.astype(str).str.lower())
    return kb_df

class Chat():
    def __init__(self) -> None:
        # self.actions = Actions()
        # self.selection = Selection()
        # self.kb = load_knowledgebase_df()
        self.history = [] 

    



    def start(self):
        domains = {}
        df = None
        row = None

        while True:
            # Get Model Output for User Input
            user_in = input()
            user_in_prefixed = f'user : {user_in}'
            self.history.append(user_in_prefixed)

            raw_output = sample([user_in_prefixed])[0]

            split_at = raw_output.find('system : ')
            system_response = raw_output[split_at:]
            belief_string = raw_output[:split_at]

            res = "I sorry i did not understand that"
            try:
                for code in belief_string.split(";"):
                    exec(code.strip())
                res = eval("f'" + belief_string.strip() + "'")
            except:
                pass
    

            self.history.append(system_response)

            print(raw_output)
            print(res)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')

    from soloist.server import *
    args.model_name_or_path = 'knowledgebase_model'
    # this is the main method from the soloist server
    main()

    chat = Chat()
    chat.start()