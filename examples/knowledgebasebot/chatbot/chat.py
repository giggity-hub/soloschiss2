import pandas as pd
from selection import Selection
from actions import Actions
from soloist_parser import parse_soloist_output


def load_knowledgebase_df():
    kb_df = pd.read_csv('data.csv')
    # make entire dataset lowercase
    kb_df = kb_df.apply(lambda x: x.astype(str).str.lower())
    return kb_df

class Chat():
    def __init__(self) -> None:
        self.actions = Actions()
        self.selection = Selection()
        self.kb = load_knowledgebase_df()
        self.history = [] 


    def start(self):
        while True:
            # Get Model Output for User Input
            user_in = input()
            user_in_prefixed = f'user : {user_in}'
            raw_output = sample(self.history[-1:])[0]

            # Parse the Raw output of the model
            belief_state_dict, system_response = parse_soloist_output(raw_output)

            # update the selection
            self.selection.update(belief_state_dict, self.kb)

            # Update the History
            self.history.append(user_in_prefixed)
            self.history.append(system_response)

            # Some Debugging Infos
            # print(f'belief_state_string : {belief_state_string}')
            print(f'belief_state_dict : {belief_state_dict}')
   



            predicted_action = self.actions.find_action(system_response)
            if predicted_action:
                output = self.actions.do(predicted_action, belief_state_dict, self.selection)
            else:
                output = system_response

            print(output)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')

    from soloist.server import *
    args.model_name_or_path = 'knowledgebase_model'
    # this is the main method from the soloist server
    main()

    chat = Chat()
    chat.start()